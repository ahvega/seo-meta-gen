"""
Web content extraction module for SEO Metadata Generator
"""

import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def get_page_content(self, url: str) -> Optional[Dict]:
        """
        Extract content from a WordPress page URL
        
        Args:
            url (str): The URL of the WordPress page
            
        Returns:
            Dict: Dictionary containing extracted content elements
        """
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title
            title = soup.find('h1', class_='entry-title')
            if not title:
                title = soup.find('title')
            title = title.text.strip() if title else ''
            
            # Extract post type (from body class)
            post_type = 'post'  # default
            body_classes = soup.find('body').get('class', [])
            for class_name in body_classes:
                if class_name.startswith('post-type-'):
                    post_type = class_name.replace('post-type-', '')
                    break
            
            # Extract featured image
            featured_image = None
            img = soup.find('img', class_='wp-post-image')
            if img:
                featured_image = img.get('src', '')
            
            # Extract excerpt
            excerpt = ''
            excerpt_div = soup.find('div', class_='entry-summary')
            if excerpt_div:
                excerpt = excerpt_div.text.strip()
            
            # Extract main content
            content = ''
            content_div = soup.find('div', class_='entry-content')
            if content_div:
                content = content_div.text.strip()
            
            return {
                'title': title,
                'post_type': post_type,
                'featured_image': featured_image,
                'excerpt': excerpt,
                'content': content,
                'url': url
            }
            
        except requests.RequestException as e:
            logger.error(f"Error fetching URL {url}: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error while scraping {url}: {str(e)}")
            return None 