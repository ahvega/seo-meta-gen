from seo_meta_gen.metadata_generator import MetadataGenerator
from seo_meta_gen.config import ENDPOINT_MAP, POST_TYPE_CONTEXT, DEFAULT_CONFIG
import logging
import argparse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set logging level to DEBUG to see detailed information
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def validate_post_type(post_type: str) -> bool:
    """Validate if the post type is supported"""
    return post_type in ENDPOINT_MAP

def get_api_endpoint(post_type: str) -> str:
    """Get the API endpoint for the given post type"""
    return ENDPOINT_MAP.get(post_type)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='SEO Metadata Generator Test')
    parser.add_argument('--provider', 
                       choices=['google', 'openai', 'anthropic', 'deepseek'],
                       default='google',
                       help='LLM provider to use (default: google with gemini-1.5-flash-8b)')
    parser.add_argument('--type', 
                       choices=list(ENDPOINT_MAP.keys()),
                       default='page',
                       help='Post type to process')
    parser.add_argument('--url',
                       required=True,
                       help='URL of the page to process')
    parser.add_argument('--dry-run', 
                       action='store_true',
                       help='Run in dry-run mode without updating WordPress')
    args = parser.parse_args()
    
    # Validate post type
    if not validate_post_type(args.type):
        logger.error(f"Invalid post type: {args.type}. Supported types are: {list(ENDPOINT_MAP.keys())}")
        return
    
    # Get API endpoint for the post type
    api_endpoint = get_api_endpoint(args.type)
    logger.info(f"Using API endpoint: {api_endpoint} for post type: {args.type}")
    
    # Get context information for the post type
    post_context = POST_TYPE_CONTEXT.get(args.type, {})
    logger.info(f"Post context: {post_context}")
    
    try:
        # Initialize the metadata generator with the specified provider
        generator = MetadataGenerator()
        generator.provider = args.provider
        
        # Set the most cost-effective model for each provider
        if args.provider == 'google':
            generator.model = 'gemini-1.5-flash-8b'  # $0.1875 per 1M tokens
        elif args.provider == 'openai':
            generator.model = 'gpt-4.1-nano'  # $0.50 per 1M tokens
        elif args.provider == 'deepseek':
            generator.model = 'R1'  # $2.74 per 1M tokens
        elif args.provider == 'anthropic':
            generator.model = 'claude-3-5-haiku-20241022'  # $4.80 per 1M tokens
            
        generator._initialize_provider()
        
        # Generate metadata
        logger.info(f"Generating metadata for URL: {args.url}")
        metadata = generator.generate_metadata(page_url=args.url, post_type=args.type)
        
        if metadata:
            print("\nGenerated Metadata:")
            print("------------------")
            for key, value in metadata.items():
                print(f"{key}: {value}")
            
            # Print cost summary
            print("\nCost Summary:")
            print("------------")
            print(generator.get_cost_summary())
            
            if not args.dry_run:
                # TODO: Implement WordPress update logic here
                logger.info("WordPress update would be performed here")
        else:
            logger.error("Failed to generate metadata")
            
    except Exception as e:
        logger.error(f"Error during processing: {str(e)}")

if __name__ == "__main__":
    main() 