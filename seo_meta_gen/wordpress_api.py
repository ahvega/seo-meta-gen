"""
WordPress API client for content retrieval and updates.
"""

import logging
import requests
import json
from typing import Dict, List, Optional, Any
from .config import Config, ENDPOINT_MAP

logger = logging.getLogger(__name__)

class WordPressAPI:
    """Handles WordPress REST API communication."""
    
    def __init__(self, config: Config):
        """
        Initialize WordPress API client.
        
        Args:
            config: Configuration object containing API settings
        """
        self.config = config
        self.base_url = config.wordpress_url.rstrip('/')
        self.auth = (config.wordpress_username, config.wordpress_password)
        self.session = requests.Session()
        self.session.auth = self.auth
        
    def update_post(self, post_id: int, data: Dict[str, Any], post_type: str = 'posts') -> bool:
        """
        Update a WordPress post with new data.
        
        Args:
            post_id: WordPress post ID
            data: Dictionary containing fields to update
            post_type: Type of post to update (posts, pages, etc.)
            
        Returns:
            bool: True if update was successful
        """
        try:
            # Get the correct endpoint from ENDPOINT_MAP
            endpoint = ENDPOINT_MAP.get(post_type, post_type)
            url = f"{self.base_url}/wp-json/wp/v2/{endpoint}/{post_id}"
            response = self.session.post(url, json=data)
            
            if response.status_code == 200:
                logger.info(f"Successfully updated {post_type} {post_id}")
                return True
            else:
                logger.error(f"Failed to update {post_type} {post_id}. Status code: {response.status_code}")
                logger.error(f"Response: {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Error updating {post_type} {post_id}: {str(e)}")
            return False
            
    def batch_update_posts(self, updates: List[Dict], post_type: str = 'posts') -> bool:
        """
        Update multiple posts in a single batch request.
        
        Args:
            updates (List[Dict]): List of dictionaries containing post_id and data to update
            post_type (str): Post type (default: 'posts')
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get the correct endpoint for the post type
            endpoint_slug = ENDPOINT_MAP.get(post_type, post_type)
            logger.info(f"Using endpoint slug: {endpoint_slug} for post type: {post_type}")
            
            # Debug log the updates
            logger.info("Received updates:")
            for i, update in enumerate(updates, 1):
                logger.info(f"Update {i}: {json.dumps(update, indent=2, ensure_ascii=False)}")
            
            # Prepare batch request
            batch_requests = []
            for update in updates:
                if 'post_id' in update and 'data' in update:
                    batch_requests.append({
                        'method': 'POST',
                        'path': f'/wp/v2/{endpoint_slug}/{update["post_id"]}',
                        'body': update['data']
                    })
                else:
                    logger.warning(f"Invalid update format: {json.dumps(update, indent=2, ensure_ascii=False)}")
            
            if not batch_requests:
                logger.warning("No valid updates to process in batch")
                return False
                
            # Log the complete batch request
            batch_data = {
                'requests': batch_requests
            }
            logger.info("Complete batch request body:")
            logger.info(json.dumps(batch_data, indent=2, ensure_ascii=False))
            
            response = self.session.post(
                f"{self.config.wordpress_url}/wp-json/batch/v1",
                json=batch_data
            )
            
            if response.status_code == 207:
                # Multi-status response - check individual responses
                results = response.json()
                all_success = True
                for i, result in enumerate(results['responses'], 1):
                    if result['status'] >= 400:
                        all_success = False
                        logger.error(f"Batch request {i} failed with status {result['status']}: {result.get('body', {}).get('message', 'No error message')}")
                    else:
                        logger.info(f"Batch request {i} succeeded with status {result['status']}")
                return all_success
            else:
                logger.error(f"Batch request failed with status {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Error in batch update: {e}")
            return False
            
    # ... existing code ... 