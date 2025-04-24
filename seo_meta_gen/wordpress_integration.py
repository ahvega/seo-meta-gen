"""
WordPress REST API integration module
"""

import os
from typing import Dict, Optional
import requests
from dotenv import load_dotenv
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

class WordPressIntegration:
    def __init__(self):
        self.base_url = os.getenv('WORDPRESS_URL')
        self.username = os.getenv('WORDPRESS_USERNAME')
        self.password = os.getenv('WORDPRESS_PASSWORD')
        
        if not all([self.base_url, self.username, self.password]):
            raise ValueError("Missing required WordPress credentials in environment variables")
        
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def _get_post_id_from_url(self, url: str) -> Optional[int]:
        """
        Get WordPress post ID from URL
        
        Args:
            url (str): The URL of the WordPress post
            
        Returns:
            Optional[int]: The post ID if found, None otherwise
        """
        try:
            # Remove trailing slash if present
            url = url.rstrip('/')
            
            # Make a request to the WordPress REST API to search for the post
            response = self.session.get(
                f"{self.base_url}/wp-json/wp/v2/posts",
                params={'search': url}
            )
            response.raise_for_status()
            
            posts = response.json()
            if posts:
                return posts[0]['id']
            
            return None
            
        except requests.RequestException as e:
            logger.error(f"Error getting post ID: {str(e)}")
            return None

    def update_seo_metadata(self, url: str, metadata: Dict) -> bool:
        """
        Update SEO metadata for a WordPress post
        
        Args:
            url (str): The URL of the WordPress post
            metadata (Dict): Dictionary containing SEO metadata
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        try:
            post_id = self._get_post_id_from_url(url)
            if not post_id:
                logger.error(f"Could not find post ID for URL: {url}")
                return False
            
            # Prepare the metadata update payload
            update_data = {
                'meta': {
                    'rank_math_title': metadata['meta_title'],
                    'rank_math_description': metadata['meta_description'],
                    'rank_math_focus_keyword': metadata['focus_keyword'],
                    'rank_math_canonical_url': metadata['canonical_url'],
                    'rank_math_og_title': metadata['og_title'],
                    'rank_math_og_description': metadata['og_description'],
                    'rank_math_twitter_title': metadata['twitter_title'],
                    'rank_math_twitter_description': metadata['twitter_description']
                }
            }
            
            # Update the post metadata
            response = self.session.post(
                f"{self.base_url}/wp-json/wp/v2/posts/{post_id}",
                json=update_data
            )
            response.raise_for_status()
            
            logger.info(f"Successfully updated SEO metadata for post ID: {post_id}")
            return True
            
        except requests.RequestException as e:
            logger.error(f"Error updating SEO metadata: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error while updating SEO metadata: {str(e)}")
            return False 