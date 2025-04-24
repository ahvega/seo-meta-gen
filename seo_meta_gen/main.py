"""
Main script for SEO metadata generation
"""

import logging
import argparse
import json
from .batch_processor import BatchProcessor
from .metadata_generator import MetadataGenerator
from .url_manager import URLManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the SEO metadata generation process."""
    parser = argparse.ArgumentParser(description='SEO Metadata Generator')
    parser.add_argument('--provider', type=str, default='google', 
                       choices=['openai', 'google', 'deepseek', 'anthropic'],
                       help='AI provider to use (default: google)')
    parser.add_argument('--post-type', type=str, 
                       help='Specific post type to process (default: all)')
    parser.add_argument('--source', type=str, default='my_site_urls.json',
                       help='Source file to process (URL list or metadata file) (default: my_site_urls.json)')
    parser.add_argument('--write-to-db', action='store_true',
                       help='Write generated metadata to WordPress database')
    parser.add_argument('--dry-run', action='store_true',
                       help='Run in dry-run mode without making actual changes')
    parser.add_argument('--taxonomy', type=str,
                       help='Taxonomy to process')
    parser.add_argument('--terms', nargs='+',
                       help='Specific terms to process')
    
    args = parser.parse_args()
    
    try:
        if args.taxonomy:
            # Process taxonomy terms
            generator = MetadataGenerator(provider=args.provider)
            results = generator.process_taxonomies(args.taxonomy, args.terms)
            
            # Save results
            if results:
                output_file = f"generated_metadata_{args.taxonomy}.json"
                with open(f"output/{output_file}", "w", encoding="utf-8") as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
                logger.info(f"Saved results to output/{output_file}")
            else:
                logger.warning("No results generated")
        else:
            # Process URLs or metadata file
            processor = BatchProcessor(
                url_list_file=args.source,
                provider=args.provider,
                post_type=args.post_type,
                write_to_db=args.write_to_db,
                dry_run=args.dry_run
            )
            
            # Log appropriate information based on mode
            if args.write_to_db:
                logger.info(f"Writing to database (dry run: {args.dry_run})")
            else:
                logger.info(f"Starting process with provider: {args.provider}")
                if args.post_type:
                    logger.info(f"Processing post type: {args.post_type}")
                
            success = processor.run()
            
            if success:
                logger.info("Process completed successfully")
            else:
                logger.error("Process failed")
            
    except Exception as e:
        logger.error(f"Error in main process: {e}")
        raise

if __name__ == "__main__":
    main() 