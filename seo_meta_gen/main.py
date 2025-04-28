"""
Main entry point for SEO metadata generation tool
"""

import argparse
import logging
from typing import Optional
from .config import Config, load_config, RegionConfig
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='SEO Metadata Generator')
    
    # Required arguments
    parser.add_argument('--phase', type=str, required=True,
                      choices=['discover-content', 'generate-metadata', 'enhance-sentiment', 
                              'enhance-value-prop', 'enhance-region', 'write-to-db'],
                      help='Phase of the process to execute')
    parser.add_argument('--post-type', type=str, required=True,
                      help='Type of posts to process')
    
    # Phase-specific arguments
    parser.add_argument('--url-file', type=str,
                      help='File containing URLs to process (required for discover-content phase)')
    parser.add_argument('--input-file', type=str,
                      help='Input file from previous phase (required for all phases except discover-content)')
    parser.add_argument('--output-file', type=str,
                      help='Output file to write results to')
    
    # Optional arguments
    parser.add_argument('--provider', type=str, default='google',
                      choices=['google', 'openai', 'anthropic', 'deepseek'],
                      help='AI provider to use (default: google)')
    parser.add_argument('--region', type=str, default='global',
                      help='Region for content targeting (default: global)')
    parser.add_argument('--mode', type=str, default='full',
                      choices=['full', 'partial'],
                      help='Processing mode (default: full)')
    parser.add_argument('--debug', action='store_true',
                      help='Enable debug logging')
    
    return parser.parse_args()

def main():
    """Main execution function"""
    args = parse_args()
    
    # Set up logging
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Load configuration with required parameters
    config = Config(
        wordpress_url=os.getenv('WORDPRESS_URL', ''),
        wordpress_username=os.getenv('WORDPRESS_USERNAME', ''),
        wordpress_password=os.getenv('WORDPRESS_PASSWORD', ''),
        preferred_ai_provider=args.provider
    )
    
    # Update config with command line arguments
    config.provider = args.provider
    
    # Set up region configuration if specified
    if args.region != 'global':
        config.region_config = RegionConfig(
            region=args.region,
            language='es'  # You might want to make this configurable
        )
    
    # Execute appropriate phase
    try:
        if args.phase == 'discover-content':
            if not args.url_file:
                raise ValueError("--url-file is required for discover-content phase")
            from .content_discovery import ContentDiscovery
            discoverer = ContentDiscovery(config)
            discoverer.process_urls(args.url_file, args.post_type)
            
        elif args.phase == 'generate-metadata':
            if not args.input_file:
                raise ValueError("--input-file is required for generate-metadata phase")
            from .batch_processor import BatchProcessor
            from .metadata_generator import MetadataGenerator
            generator = MetadataGenerator(config)
            processor = BatchProcessor(generator, config)
            processor.process_batch(args.input_file, args.post_type, args.mode)
            
        elif args.phase == 'enhance-sentiment':
            if not args.input_file:
                raise ValueError("--input-file is required for enhance-sentiment phase")
            from .metadata_generator import MetadataGenerator
            # Create a minimal config without any AI provider
            sentiment_config = Config(
                wordpress_url=os.getenv('WORDPRESS_URL', ''),
                wordpress_username=os.getenv('WORDPRESS_USERNAME', ''),
                wordpress_password=os.getenv('WORDPRESS_PASSWORD', ''),
                preferred_ai_provider=None  # Explicitly set to None to avoid AI initialization
            )
            sentiment_config.region_config = config.region_config
            generator = MetadataGenerator(sentiment_config)
            generator.enhance_metadata_with_sentiment(args.input_file)
            
        elif args.phase == 'enhance-value-prop':
            if not args.input_file:
                raise ValueError("--input-file is required for enhance-value-prop phase")
            from .metadata_generator import MetadataGenerator
            # Create a minimal config without AI provider for value proposition
            value_prop_config = Config(
                wordpress_url=os.getenv('WORDPRESS_URL', ''),
                wordpress_username=os.getenv('WORDPRESS_USERNAME', ''),
                wordpress_password=os.getenv('WORDPRESS_PASSWORD', ''),
                preferred_ai_provider='none'  # No AI provider needed for value prop
            )
            value_prop_config.region_config = config.region_config
            generator = MetadataGenerator(value_prop_config)
            generator.enhance_metadata_with_value_prop(args.input_file)
            
        elif args.phase == 'enhance-region':
            if not args.input_file:
                raise ValueError("--input-file is required for enhance-region phase")
            from .metadata_generator import MetadataGenerator
            # Create a minimal config without AI provider for region enhancement
            region_config = Config(
                wordpress_url=os.getenv('WORDPRESS_URL', ''),
                wordpress_username=os.getenv('WORDPRESS_USERNAME', ''),
                wordpress_password=os.getenv('WORDPRESS_PASSWORD', ''),
                preferred_ai_provider='none'  # No AI provider needed for region
            )
            region_config.region_config = config.region_config
            generator = MetadataGenerator(region_config)
            generator.enhance_metadata_with_region(args.input_file)
            
        elif args.phase == 'write-to-db':
            if not args.input_file:
                raise ValueError("--input-file is required for write-to-db phase")
            from .db_writer import DatabaseWriter
            writer = DatabaseWriter(config)
            writer.write_batch(args.input_file, args.mode)
            
    except Exception as e:
        logger.error(f"Error during {args.phase} phase: {str(e)}")
        raise

if __name__ == '__main__':
    main() 