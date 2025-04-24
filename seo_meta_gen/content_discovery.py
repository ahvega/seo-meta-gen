"""
Content Discovery Module

This module handles the discovery of WordPress content types and taxonomies through the REST API.
It filters out system types and identifies custom post types for processing.
"""

import logging
import requests
from typing import Dict, List, Set
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Post types that should be excluded as they are not website content
NON_CONTENT_TYPES = {
    'attachment',  # Media attachments
    'nav_menu_item',  # Menu items
    'revision',  # Post revisions
    'custom_css',  # Custom CSS
    'customize_changeset',  # Customizer changes
    'oembed_cache',  # oEmbed cache
    'user_request',  # User data requests
    'wp_block',  # Reusable blocks
    'wp_template',  # Templates
    'wp_template_part',  # Template parts
    'wp_global_styles',  # Global styles
    'wp_navigation',  # Navigation menus
    'elementor_library',  # Elementor templates
    'elementor_font',  # Elementor fonts
    'elementor_icons',  # Elementor icons
}

class ContentDiscovery:
    """Handles discovery of WordPress content types and taxonomies."""
    
    def __init__(self, base_url: str, username: str, password: str):
        """
        Initialize the ContentDiscovery class.
        
        Args:
            base_url (str): Base URL of the WordPress site
            username (str): WordPress username for API authentication
            password (str): Application password for API authentication
        """
        self.base_url = base_url.rstrip('/')
        self.auth = (username, password)
        self.session = requests.Session()
        self.session.auth = self.auth
        
    def get_post_types(self) -> Dict[str, Dict]:
        """
        Discover all available post types from the WordPress REST API.
        
        Returns:
            Dict[str, Dict]: Dictionary of post types and their properties
        """
        try:
            response = self.session.get(f"{self.base_url}/wp-json/wp/v2/types")
            response.raise_for_status()
            post_types = response.json()
            
            # Filter out system types, non-content types, and Elementor types
            filtered_types = {
                name: props for name, props in post_types.items()
                if (not name.startswith(('wp_', 'e_')) and  # Exclude wp_ and e_ prefixed types
                    name not in NON_CONTENT_TYPES and  # Exclude non-content types
                    not any(name.startswith(prefix) for prefix in ['elementor_', 'e-']))  # Exclude Elementor types
            }
            
            logger.info(f"Discovered {len(filtered_types)} content post types")
            if filtered_types:
                logger.info(f"Content post types: {', '.join(filtered_types.keys())}")
            return filtered_types
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error discovering post types: {e}")
            return {}
            
    def get_taxonomies(self) -> Dict[str, Dict]:
        """
        Discover category-related taxonomies from the WordPress REST API.
        
        Returns:
            Dict[str, Dict]: Dictionary of category taxonomies and their properties
        """
        try:
            response = self.session.get(f"{self.base_url}/wp-json/wp/v2/taxonomies")
            response.raise_for_status()
            taxonomies = response.json()
            
            # Filter to only include category-related taxonomies
            filtered_taxonomies = {
                name: props for name, props in taxonomies.items()
                if (name == 'category' or  # Default WordPress category
                    name.endswith('_category') or  # Custom category taxonomies
                    name == 'stm_service_category')  # Specific custom category
            }
            
            logger.info(f"Discovered {len(filtered_taxonomies)} category taxonomies")
            if filtered_taxonomies:
                logger.info(f"Category taxonomies: {', '.join(filtered_taxonomies.keys())}")
            return filtered_taxonomies
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error discovering taxonomies: {e}")
            return {}
            
    def get_custom_post_types(self) -> Set[str]:
        """
        Identify custom post types (prefixed with 'stm_').
        
        Returns:
            Set[str]: Set of custom post type names
        """
        post_types = self.get_post_types()
        custom_types = {
            name for name in post_types.keys()
            if name.startswith('stm_')
        }
        
        logger.info(f"Found {len(custom_types)} custom post types")
        return custom_types
        
    def get_items_for_type(self, post_type: str, post_type_props: Dict) -> List[str]:
        """
        Get all items of a specific post type or taxonomy.
        
        Args:
            post_type (str): The post type or taxonomy to get items for
            post_type_props (Dict): Properties of the post type/taxonomy including rest_base
            
        Returns:
            List[str]: List of URLs for the post type/taxonomy items
        """
        try:
            items = []
            page = 1
            per_page = 100
            
            # Get the correct endpoint from rest_base
            rest_base = post_type_props.get('rest_base', post_type)
            logger.info(f"Using rest_base '{rest_base}' for post type '{post_type}'")
            
            while True:
                try:
                    response = self.session.get(
                        f"{self.base_url}/wp-json/wp/v2/{rest_base}",
                        params={'page': page, 'per_page': per_page, '_fields': 'link'}
                    )
                    response.raise_for_status()
                    
                    batch = response.json()
                    if not batch:
                        break
                        
                    # Handle both list and dict responses
                    if isinstance(batch, list):
                        # For taxonomies, the items might be direct URLs
                        if isinstance(batch[0], str):
                            items.extend(batch)
                        else:
                            items.extend(item.get('link') for item in batch if item.get('link'))
                    elif isinstance(batch, dict):
                        items.extend(batch.get('link', []))
                    
                    # Check if there are more pages
                    total_pages = int(response.headers.get('X-WP-TotalPages', 1))
                    if page >= total_pages:
                        break
                        
                    page += 1
                    
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 400 and 'page' in str(e):
                        # If we get a 400 error for page parameter, assume we've reached the end
                        break
                    else:
                        raise
                
            logger.info(f"Found {len(items)} items for post type: {post_type}")
            return items
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting items for post type {post_type}: {e}")
            return []
            
    def discover_all_content(self) -> Dict[str, List[str]]:
        """
        Discover all content URLs organized by post type and taxonomies.
        
        Returns:
            Dict[str, List[str]]: Dictionary mapping post types and taxonomies to their URLs
        """
        content_map = {}
        
        # First discover post types
        post_types = self.get_post_types()
        logger.info("Discovering content for post types...")
        for post_type, props in post_types.items():
            items = self.get_items_for_type(post_type, props)
            if items:
                content_map[post_type] = items
                
        logger.info(f"Discovered content for {len(content_map)} post types")
        
        # Then discover taxonomies
        taxonomies = self.get_taxonomies()
        logger.info("Discovering content for taxonomies...")
        for taxonomy, props in taxonomies.items():
            items = self.get_items_for_type(taxonomy, props)
            if items:
                content_map[f"taxonomy_{taxonomy}"] = items
                
        total_items = sum(len(urls) for urls in content_map.values())
        logger.info(f"Total discovered items: {total_items}")
        return content_map 