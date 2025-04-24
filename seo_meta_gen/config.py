"""
Configuration settings for SEO Metadata Generator
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

# Mapping of post types to their API endpoints
ENDPOINT_MAP = {
    'post': 'posts',
    'page': 'pages',
    'stm_service': 'servicios',  # Spanish translation for services
    'stm_staff': 'equipo',       # Spanish translation for team/staff
    'stm_testimonials': 'testimoniales',  # Spanish translation for testimonials
    'stm_service_category': 'categorias-servicio',  # Correct taxonomy for service categories
    'category': 'categories',    # Standard WordPress categories
    'post_tag': 'tags'          # Standard WordPress tags
}

# LLM context information for different post types
POST_TYPE_CONTEXT = {
    'post': {
        'description': 'A blog post or article',
        'seo_focus': 'Content quality, readability, and engagement',
        'metadata_priority': ['title', 'description', 'keywords', 'content']
    },
    'page': {
        'description': 'A static page',
        'seo_focus': 'Clear value proposition and conversion optimization',
        'metadata_priority': ['title', 'description', 'keywords']
    },
    'stm_service': {
        'description': 'A service offering',
        'seo_focus': 'Service benefits, features, and unique selling points',
        'metadata_priority': ['title', 'description', 'features', 'benefits']
    },
    'stm_staff': {
        'description': 'A team member profile',
        'seo_focus': 'Professional expertise and personal connection',
        'metadata_priority': ['name', 'role', 'expertise', 'bio']
    },
    'stm_testimonials': {
        'description': 'A client testimonial',
        'seo_focus': 'Social proof and credibility',
        'metadata_priority': ['client_name', 'service', 'testimonial', 'rating']
    },
    'stm_service_category': {
        'description': 'A service category',
        'seo_focus': 'Category overview and service grouping',
        'metadata_priority': ['title', 'description', 'related_services']
    },
    'category': {
        'description': 'A blog post category',
        'seo_focus': 'Category overview and content organization',
        'metadata_priority': ['title', 'description', 'related_posts']
    },
    'post_tag': {
        'description': 'A blog post tag',
        'seo_focus': 'Tag relevance and content association',
        'metadata_priority': ['title', 'description', 'related_posts']
    }
}

# Default configuration values
DEFAULT_CONFIG = {
    'max_content_length': 1000,  # Maximum characters to process
    'min_content_length': 100,   # Minimum characters to process
    'default_post_type': 'post',
    'supported_post_types': list(ENDPOINT_MAP.keys())
}

@dataclass
class Config:
    """Configuration class for SEO Metadata Generator."""
    
    # WordPress API settings
    wordpress_url: str
    wordpress_username: str
    wordpress_password: str
    
    # Content settings
    max_content_length: int = DEFAULT_CONFIG['max_content_length']
    min_content_length: int = DEFAULT_CONFIG['min_content_length']
    default_post_type: str = DEFAULT_CONFIG['default_post_type']
    supported_post_types: List[str] = field(default_factory=lambda: list(ENDPOINT_MAP.keys()))
    
    # AI settings
    provider: str = 'google'
    model: Optional[str] = None
    temperature: float = 0.7
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if not self.wordpress_url:
            raise ValueError("WordPress URL is required")
        if not self.wordpress_username:
            raise ValueError("WordPress username is required")
        if not self.wordpress_password:
            raise ValueError("WordPress password is required")
        if self.max_content_length < self.min_content_length:
            raise ValueError("max_content_length must be greater than min_content_length") 