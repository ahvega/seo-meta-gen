"""
Database writer module for updating WordPress posts with metadata.
"""

import logging
from typing import Dict, List, Optional
from seo_meta_gen.wordpress_api import WordPressAPI
from seo_meta_gen.config import Config

logger = logging.getLogger(__name__)

class DatabaseWriter:
    """Handles writing metadata updates to the WordPress database."""
    
    def __init__(self, config: Config, dry_run: bool = True):
        """
        Initialize the database writer.
        
        Args:
            config: Configuration object containing WordPress credentials
            dry_run: If True, only log updates without making actual changes
        """
        self.api = WordPressAPI(config)
        self.dry_run = dry_run
        logger.info(f"Database writer initialized in {'dry run' if dry_run else 'live'} mode")
    
    def update_post_metadata(self, post_id: int, metadata: Dict, post_type: str = 'posts') -> bool:
        """
        Update a single post's metadata.
        
        Args:
            post_id: WordPress post ID
            metadata: Dictionary of metadata fields to update
            post_type: Type of post to update (posts, pages, etc.)
            
        Returns:
            bool: True if update was successful or in dry run mode
        """
        if not post_id or not metadata:
            logger.warning(f"Invalid update request: post_id={post_id}, metadata={metadata}")
            return False
            
        if self.dry_run:
            logger.info(f"[DRY RUN] Would update {post_type} {post_id} with metadata: {metadata}")
            return True
            
        try:
            # Map metadata to Rank Math fields
            rank_math_data = {
                'rank_math': {
                    'title': metadata.get('meta_title', ''),
                    'description': metadata.get('meta_description', ''),
                    'focus_keyword': metadata.get('focus_keyword', ''),
                    'canonical_url': metadata.get('canonical_url', ''),
                    'og_title': metadata.get('og_title', ''),
                    'og_description': metadata.get('og_description', ''),
                    'twitter_title': metadata.get('twitter_title', ''),
                    'twitter_description': metadata.get('twitter_description', '')
                }
            }
            
            success = self.api.update_post(post_id, rank_math_data, post_type)
            if success:
                logger.info(f"Successfully updated {post_type} {post_id}")
            else:
                logger.error(f"Failed to update {post_type} {post_id}")
            return success
        except Exception as e:
            logger.error(f"Error updating {post_type} {post_id}: {str(e)}")
            return False
    
    def batch_update(self, updates: List[Dict], post_type: str) -> Dict[str, int]:
        """
        Process a batch of metadata updates.
        
        Args:
            updates: List of dictionaries containing post_id and metadata
            post_type: The type of post being updated (e.g., 'page', 'post')
            
        Returns:
            Dict containing statistics about the batch update
        """
        stats = {
            'total': len(updates),
            'success': 0,
            'failed': 0,
            'skipped': 0
        }
        
        if self.dry_run:
            logger.info(f"[DRY RUN] Would update {len(updates)} items")
            stats['success'] = len(updates)
            return stats
            
        try:
            # Prepare batch updates
            batch_updates = []
            for update in updates:
                post_id = update.get('post_id')
                metadata = update.get('metadata')
                
                if not post_id or not metadata:
                    logger.warning(f"Skipping invalid update: {update}")
                    stats['skipped'] += 1
                    continue
                    
                # Map metadata to Rank Math fields
                rank_math_data = {
                    'rank_math': {
                        'title': metadata.get('meta_title', ''),
                        'description': metadata.get('meta_description', ''),
                        'focus_keyword': metadata.get('focus_keyword', ''),
                        'canonical_url': metadata.get('canonical_url', ''),
                        'og_title': metadata.get('og_title', ''),
                        'og_description': metadata.get('og_description', ''),
                        'twitter_title': metadata.get('twitter_title', ''),
                        'twitter_description': metadata.get('twitter_description', '')
                    }
                }
                
                batch_updates.append({
                    'post_id': post_id,
                    'data': rank_math_data
                })
            
            # Process batch updates
            if batch_updates:
                logger.info(f"Processing updates for post type: {post_type}")
                success = self.api.batch_update_posts(batch_updates, post_type)
                if success:
                    stats['success'] = len(batch_updates)
                else:
                    stats['failed'] = len(batch_updates)
            else:
                stats['failed'] = len(updates)
            
            # Log detailed stats
            logger.info(f"Batch update completed: {stats}")
            if stats['failed'] > 0:
                logger.error(f"Failed to update {stats['failed']} items")
            if stats['skipped'] > 0:
                logger.warning(f"Skipped {stats['skipped']} items")
            if stats['success'] > 0:
                logger.info(f"Successfully updated {stats['success']} items")
            
            return stats
            
        except Exception as e:
            logger.error(f"Error processing batch update: {str(e)}")
            stats['failed'] = len(updates)
            return stats 