"""
Batch Processor Module

This module handles batch processing of URLs for metadata generation and database updates.
"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional
from tqdm import tqdm
from .url_manager import URLManager
from .metadata_generator import MetadataGenerator
from .config import POST_TYPE_CONTEXT, Config, ENDPOINT_MAP
from .db_writer import DatabaseWriter
from .wordpress_api import WordPressAPI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BatchProcessor:
    """Handles batch processing of URLs for metadata generation and database updates."""
    
    def __init__(self, url_list_file: str = "my_site_urls.json", 
                 provider: str = "google", post_type: Optional[str] = None,
                 write_to_db: bool = False, dry_run: bool = True):
        """
        Initialize the BatchProcessor.
        
        Args:
            url_list_file (str): Name of the source file to process (URL list or metadata file)
            provider (str): AI provider to use
            post_type (Optional[str]): Specific post type to process
            write_to_db (bool): Whether to write to database
            dry_run (bool): Whether to run in dry-run mode
        """
        self.source_file = url_list_file
        self.post_type = post_type
        self.write_to_db = write_to_db
        self.dry_run = dry_run
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Initialize config if writing to database
        if write_to_db:
            wordpress_url = os.getenv('WORDPRESS_URL')
            wordpress_username = os.getenv('WORDPRESS_USERNAME')
            wordpress_password = os.getenv('WORDPRESS_PASSWORD')
            
            if not all([wordpress_url, wordpress_username, wordpress_password]):
                raise ValueError("WordPress credentials not found in environment variables. Please check your .env file.")
                
            self.config = Config(
                wordpress_url=wordpress_url,
                wordpress_username=wordpress_username,
                wordpress_password=wordpress_password
            )
        else:
            self.config = None
            
        # Only initialize metadata generator if we're not just writing to DB
        if not write_to_db:
            self.metadata_generator = MetadataGenerator(provider=provider)
        else:
            self.metadata_generator = None
            
    def run(self) -> bool:
        """
        Run the complete batch processing workflow.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Load source file
            source_data = self._load_source_file()
            if not source_data:
                logger.error("Failed to load source file")
                return False
                
            if self.write_to_db:
                return self._write_to_database(source_data)
            else:
                return self._process_metadata(source_data)
                
        except Exception as e:
            logger.error(f"Error in batch processing: {e}")
            return False
            
    def _write_to_database(self, metadata_data: Dict) -> bool:
        """
        Write metadata to WordPress database.
        
        Args:
            metadata_data (Dict): Dictionary containing metadata to write
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            logger.info(f"Starting database write process (dry run: {self.dry_run})")
            
            # Initialize database writer with config
            db_writer = DatabaseWriter(config=self.config, dry_run=self.dry_run)
            
            # Process each post type
            for post_type, items in metadata_data.items():
                logger.info(f"Processing {len(items)} items for post type: {post_type}")
                
                # Prepare updates
                updates = []
                for item in items:
                    if 'metadata' in item and 'post_id' in item:
                        updates.append({
                            'post_id': item['post_id'],
                            'metadata': item['metadata']
                        })
                    else:
                        logger.warning(f"Missing post_id or metadata in item: {item}")
                
                # Write to database
                stats = db_writer.batch_update(updates, post_type)
                
                # Log results
                if self.dry_run:
                    logger.info(f"[DRY RUN] Would have updated {stats['total']} items")
                    logger.info(f"Success: {stats['success']}, Failed: {stats['failed']}, Skipped: {stats['skipped']}")
                else:
                    logger.info(f"Successfully updated {stats['success']} items")
                    if stats['failed'] > 0:
                        logger.warning(f"Failed to update {stats['failed']} items")
                    if stats['skipped'] > 0:
                        logger.warning(f"Skipped {stats['skipped']} items")
            
            logger.info("Database write process completed")
            return True
            
        except Exception as e:
            logger.error(f"Error writing to database: {e}")
            return False
            
    def _get_post_id_from_url(self, url: str, post_type: str) -> Optional[int]:
        """
        Get WordPress post ID from URL.
        
        Args:
            url (str): Post URL
            post_type (str): Post type
            
        Returns:
            Optional[int]: Post ID if found, None otherwise
        """
        try:
            # Initialize WordPress API
            api = WordPressAPI(self.config)
            
            # Get the slug from the URL
            slug = url.rstrip('/').split('/')[-1]
            
            # Search for the post by slug using the correct endpoint
            endpoint_slug = ENDPOINT_MAP.get(post_type, post_type)
            endpoint = f"wp/v2/{endpoint_slug}"
            params = {'slug': slug}
            response = api.session.get(f"{self.config.wordpress_url}/wp-json/{endpoint}", params=params)
            
            if response.status_code == 200:
                posts = response.json()
                if posts and isinstance(posts, list) and len(posts) > 0:
                    # Ensure the returned post matches the requested post_type
                    # Although the endpoint filter should handle this, it's a good safeguard
                    for post in posts:
                        if post.get('type') == post_type:
                            return post['id']
                    logger.warning(f"Found post(s) for slug '{slug}' but none matched type '{post_type}'. URL: {url}")
                    return None # Found posts, but not the right type
                else:
                    logger.warning(f"No posts found for slug '{slug}' at endpoint '{endpoint}'. URL: {url}")
                    return None # No posts found at all
            else:
                logger.warning(f"API error {response.status_code} when searching for slug '{slug}' at endpoint '{endpoint}'. URL: {url}")
                return None
            
        except Exception as e:
            logger.error(f"Error getting post ID for URL {url}: {e}")
            return None
            
    def _process_metadata(self, source_data: Dict) -> bool:
        """
        Process URLs and generate metadata.
        
        Args:
            source_data (Dict): Source data to process
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # If source is a metadata file, return it directly
            if self._is_metadata_file(source_data):
                return self.save_results(source_data)
                
            # Filter by post type if specified
            if self.post_type:
                if self.post_type not in source_data:
                    logger.error(f"Post type {self.post_type} not found in source data")
                    return False
                source_data = {self.post_type: source_data[self.post_type]}
                
            # Initialize results structure
            results = {post_type: [] for post_type in source_data.keys()}
            
            # Process each post type
            for post_type, urls in source_data.items():
                logger.info(f"Processing {len(urls)} URLs for post type: {post_type}")
                
                # Process each URL
                for url in tqdm(urls, desc=f"Processing {post_type}"):
                    try:
                        # Generate metadata
                        metadata = self.metadata_generator.generate_metadata(url, post_type)
                        if metadata:
                            results[post_type].append({
                                "url": url,
                                "metadata": metadata
                            })
                            
                    except Exception as e:
                        logger.error(f"Error processing URL {url}: {e}")
                        
            return self.save_results(results)
            
        except Exception as e:
            logger.error(f"Error processing metadata: {e}")
            return False
            
    def _load_source_file(self) -> Optional[Dict]:
        """
        Load the source file (URL list or metadata file).
        
        Returns:
            Optional[Dict]: Loaded data or None if error
        """
        try:
            file_path = Path(self.source_file)
            if not file_path.exists():
                logger.error(f"Source file not found: {file_path}")
                return None
                
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            logger.info(f"Loaded source file: {file_path}")
            return data
            
        except Exception as e:
            logger.error(f"Error loading source file: {e}")
            return None
            
    def _is_metadata_file(self, data: Dict) -> bool:
        """
        Check if the loaded data is a metadata file.
        
        Args:
            data (Dict): Loaded data to check
            
        Returns:
            bool: True if data is a metadata file
        """
        # Check if the data structure matches metadata format
        if not isinstance(data, dict):
            return False
            
        for post_type, items in data.items():
            if not isinstance(items, list):
                return False
            for item in items:
                if not isinstance(item, dict) or 'metadata' not in item:
                    return False
                    
        return True
        
    def save_results(self, results: Dict[str, List[Dict]], filename: str = "generated_metadata.json") -> bool:
        """
        Save generated metadata to a JSON file.
        
        Args:
            results (Dict[str, List[Dict]]): Generated metadata
            filename (str): Name of the output file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Customize filename if processing specific post type
            if self.post_type:
                filename = f"generated_metadata_{self.post_type}.json"
                
            file_path = self.output_dir / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
                
            logger.info(f"Saved results to {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            return False 