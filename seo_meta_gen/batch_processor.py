"""
Batch processing module for SEO metadata generation
"""

import logging
import json
import os
from typing import Optional, List, Dict, Any
from tqdm import tqdm
from .metadata_generator import MetadataGenerator
from .config import Config

logger = logging.getLogger(__name__)

class BatchProcessor:
    """Handles batch processing of content for metadata generation"""
    
    def __init__(self, metadata_generator: MetadataGenerator, config: Config):
        """
        Initialize the batch processor
        
        Args:
            metadata_generator: Instance of MetadataGenerator
            config: Configuration instance
        """
        self.metadata_generator = metadata_generator
        self.config = config
        self.batch_size = config.batch_size
        
    def process_batch(self, input_file: str, post_type: str, mode: str = 'full') -> None:
        """
        Process a batch of URLs and generate metadata
        
        Args:
            input_file: Path to input file containing URLs
            post_type: Type of posts to process
            mode: Processing mode ('full' or 'partial')
        """
        try:
            # Load URLs from input file
            with open(input_file, 'r') as f:
                data = json.load(f)
            
            # Handle both list and dictionary formats
            if isinstance(data, list):
                # If it's a list, take the first item (assuming it's a dictionary)
                if data and isinstance(data[0], dict):
                    data = data[0]
                else:
                    logger.error("Invalid input format: Expected list containing dictionary")
                    return
            
            # Extract URLs for the specified post type
            urls = data.get(post_type, [])
            if not urls:
                logger.warning(f"No URLs found for post type: {post_type}")
                return
            
            logger.info(f"Processing {len(urls)} URLs in batches of {self.batch_size}")
            
            results = []
            for i in tqdm(range(0, len(urls), self.batch_size)):
                batch = urls[i:i + self.batch_size]
                batch_results = self._process_url_batch(batch, post_type, mode)
                results.extend(batch_results)
            
            # Create output directory if it doesn't exist
            os.makedirs('output', exist_ok=True)
            
            # Save results
            output_file = f"output/generated_metadata_{post_type}.json"
            self._write_results(results, output_file)
            
        except Exception as e:
            logger.error(f"Error processing batch: {str(e)}")
            raise
            
    def _process_url_batch(self, urls: List[str], post_type: str, mode: str) -> List[Dict[str, Any]]:
        """
        Process a batch of URLs
        
        Args:
            urls: List of URLs to process
            post_type: Type of posts
            mode: Processing mode
            
        Returns:
            List of generated metadata
        """
        results = []
        for url in urls:
            try:
                metadata = self.metadata_generator.generate_metadata(url, post_type)
                if metadata:
                    results.append({
                        'url': url,
                        'metadata': metadata,
                        'post_id': metadata.get('post_id')
                    })
            except Exception as e:
                logger.error(f"Error processing URL {url}: {str(e)}")
                continue
        return results 

    def _write_results(self, results: Dict, output_file: str) -> None:
        """Write results to output file"""
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            # Write results with proper encoding and ensure_ascii=False
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
                
            logger.info(f"Metadata generation completed. Results saved to {output_file}")
            
        except Exception as e:
            logger.error(f"Error writing results to {output_file}: {str(e)}")
            raise 