"""
Configuration module for SEO Metadata Generator
"""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

# Mapping of post types to their API endpoints
ENDPOINT_MAP = {
    'post': 'posts',
    'page': 'pages',
    'stm_service': 'servicios',
    'stm_staff': 'equipo',
    'stm_testimonials': 'testimoniales',
    'stm_service_category': 'categorias-servicio',
    'category': 'categories',
    'post_tag': 'tags'
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

@dataclass
class RegionConfig:
    """Configuration for regional settings"""
    region: str
    language: str
    currency: Optional[str] = None
    timezone: Optional[str] = None
    market_specific_terms: Dict[str, str] = field(default_factory=dict)

@dataclass
class Config:
    """Main configuration class"""
    wordpress_url: str
    wordpress_username: str
    wordpress_password: str
    preferred_ai_provider: str
    google_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    deepseek_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    
    # Content settings
    max_content_length: int = 2000
    min_content_length: int = 100
    default_post_type: str = 'post'
    supported_post_types: List[str] = field(default_factory=lambda: ['post', 'page', 'stm_service', 'stm_service_category'])
    region: str = 'global'  # Default region for SEO
    
    # AI settings
    provider: Optional[str] = None
    model: Optional[str] = None
    temperature: float = 0.7
    
    # Regional settings
    language: Optional[str] = None
    region_config: Optional[RegionConfig] = None
    
    # Batch settings
    batch_size: int = 10
    retry_attempts: int = 3
    retry_delay: int = 5
    timeout: int = 30
    debug: bool = False
    
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

def load_config(config_file: Optional[str] = None) -> Config:
    """Load configuration from file or use defaults"""
    if config_file:
        # TODO: Implement config file loading
        pass
    return Config(
        wordpress_url=os.getenv('WORDPRESS_URL', ''),
        wordpress_username=os.getenv('WORDPRESS_USERNAME', ''),
        wordpress_password=os.getenv('WORDPRESS_PASSWORD', ''),
        preferred_ai_provider=os.getenv('PREFERRED_AI_PROVIDER', 'google'),
        google_api_key=os.getenv('GOOGLE_API_KEY'),
        openai_api_key=os.getenv('OPENAI_API_KEY'),
        deepseek_api_key=os.getenv('DEEPSEEK_API_KEY'),
        anthropic_api_key=os.getenv('ANTHROPIC_API_KEY')
    )

# Default configuration instance
DEFAULT_CONFIG = Config(
    wordpress_url=os.getenv('WORDPRESS_URL', ''),
    wordpress_username=os.getenv('WORDPRESS_USERNAME', ''),
    wordpress_password=os.getenv('WORDPRESS_PASSWORD', ''),
    preferred_ai_provider=os.getenv('PREFERRED_AI_PROVIDER', 'google')
) 