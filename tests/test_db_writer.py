"""
Test cases for the database writer module.
"""

import pytest
from unittest.mock import Mock, patch
from seo_meta_gen.db_writer import DatabaseWriter
from seo_meta_gen.config import Config

@pytest.fixture
def mock_config():
    """Create a mock configuration object."""
    config = Mock(spec=Config)
    config.wordpress_url = "https://example.com"
    config.wordpress_username = "test_user"
    config.wordpress_password = "test_pass"
    return config

@pytest.fixture
def sample_metadata():
    """Create sample metadata for testing."""
    return {
        'title': 'Test Title',
        'description': 'Test Description',
        'keywords': 'test, keywords',
        'robots': 'index, follow',
        'canonical_url': 'https://example.com/test'
    }

def test_dry_run_mode(mock_config, sample_metadata):
    """Test that dry run mode doesn't make actual API calls."""
    writer = DatabaseWriter(mock_config, dry_run=True)
    
    with patch('seo_meta_gen.wordpress_api.WordPressAPI.update_post') as mock_update:
        result = writer.update_post_metadata(123, sample_metadata)
        
        # Verify no actual API call was made
        mock_update.assert_not_called()
        
        # Verify dry run was logged
        assert result is True

def test_actual_update(mock_config, sample_metadata):
    """Test actual update mode makes API calls."""
    writer = DatabaseWriter(mock_config, dry_run=False)
    
    with patch('seo_meta_gen.wordpress_api.WordPressAPI.update_post') as mock_update:
        mock_update.return_value = True
        result = writer.update_post_metadata(123, sample_metadata)
        
        # Verify API call was made
        mock_update.assert_called_once()
        
        # Verify success
        assert result is True

def test_batch_update(mock_config, sample_metadata):
    """Test batch update functionality."""
    writer = DatabaseWriter(mock_config, dry_run=True)
    
    updates = [
        {'post_id': 123, 'metadata': sample_metadata},
        {'post_id': 456, 'metadata': sample_metadata}
    ]
    
    stats = writer.batch_update(updates)
    
    # Verify statistics
    assert stats['total'] == 2
    assert stats['success'] == 2
    assert stats['failed'] == 0
    assert stats['skipped'] == 0

def test_invalid_update(mock_config):
    """Test handling of invalid updates."""
    writer = DatabaseWriter(mock_config, dry_run=True)
    
    updates = [
        {'post_id': None, 'metadata': {}},  # Invalid post_id
        {'post_id': 123, 'metadata': None}  # Invalid metadata
    ]
    
    stats = writer.batch_update(updates)
    
    # Verify statistics
    assert stats['total'] == 2
    assert stats['success'] == 0
    assert stats['failed'] == 0
    assert stats['skipped'] == 2 