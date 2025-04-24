"""
URL Manager Module

This module handles the management of URL lists, including saving, loading, and filtering URLs by post type.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class URLManager:
    """Manages URL lists for batch processing."""
    
    def __init__(self, output_dir: str = "url_lists"):
        """
        Initialize the URLManager class.
        
        Args:
            output_dir (str): Directory to store URL list files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def save_url_list(self, content_map: Dict[str, List[str]], filename: str) -> bool:
        """
        Save a URL list to a JSON file.
        
        Args:
            content_map (Dict[str, List[str]]): Dictionary mapping post types to URLs
            filename (str): Name of the file to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            file_path = self.output_dir / f"{filename}.json"
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(content_map, f, indent=2)
                
            logger.info(f"Saved URL list to {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving URL list: {e}")
            return False
            
    def load_url_list(self, filename: str) -> Optional[Dict[str, List[str]]]:
        """
        Load a URL list from a JSON file.
        
        Args:
            filename (str): Name of the file to load
            
        Returns:
            Optional[Dict[str, List[str]]]: Loaded URL list or None if error
        """
        try:
            file_path = self.output_dir / f"{filename}.json"
            with open(file_path, 'r', encoding='utf-8') as f:
                content_map = json.load(f)
                
            logger.info(f"Loaded URL list from {file_path}")
            return content_map
            
        except Exception as e:
            logger.error(f"Error loading URL list: {e}")
            return None
            
    def filter_urls_by_type(self, content_map: Dict[str, List[str]], 
                          post_types: Optional[Set[str]] = None) -> Dict[str, List[str]]:
        """
        Filter URLs by post type.
        
        Args:
            content_map (Dict[str, List[str]]): Dictionary mapping post types to URLs
            post_types (Optional[Set[str]]): Set of post types to include, None for all
            
        Returns:
            Dict[str, List[str]]: Filtered URL list
        """
        if post_types is None:
            return content_map
            
        filtered_map = {
            post_type: urls for post_type, urls in content_map.items()
            if post_type in post_types
        }
        
        logger.info(f"Filtered to {len(filtered_map)} post types")
        return filtered_map
        
    def get_all_urls(self, content_map: Dict[str, List[str]]) -> List[str]:
        """
        Get a flat list of all URLs from the content map.
        
        Args:
            content_map (Dict[str, List[str]]): Dictionary mapping post types to URLs
            
        Returns:
            List[str]: Flat list of all URLs
        """
        all_urls = []
        for urls in content_map.values():
            all_urls.extend(urls)
            
        logger.info(f"Found {len(all_urls)} total URLs")
        return all_urls
        
    def get_url_count(self, content_map: Dict[str, List[str]]) -> Dict[str, int]:
        """
        Get the count of URLs for each post type.
        
        Args:
            content_map (Dict[str, List[str]]): Dictionary mapping post types to URLs
            
        Returns:
            Dict[str, int]: Dictionary mapping post types to URL counts
        """
        counts = {
            post_type: len(urls) for post_type, urls in content_map.items()
        }
        
        logger.info(f"URL counts by post type: {counts}")
        return counts 