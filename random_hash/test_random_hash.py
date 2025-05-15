#!/usr/bin/env python3
"""
Test module for the Random Hash Generator

This script tests the functionality of the random hash generator,
ensuring it correctly generates hashes and finds those with
specific prefixes.
"""

import pytest
from unittest.mock import patch
import re

from main import generate_random_hash, find_hash_with_prefix, main


class TestRandomHashGenerator:
    """Test suite for the random hash generator module."""

    def test_generate_random_hash_length(self):
        """Test that the generated hash is 64 characters long (SHA256 hex digest)."""
        hash_value = generate_random_hash()
        assert len(hash_value) == 64, f"Hash length should be 64, got {len(hash_value)}"
        
    def test_generate_random_hash_format(self):
        """Test that the generated hash follows the hexadecimal format."""
        hash_value = generate_random_hash()
        assert re.match(r'^[0-9a-f]{64}$', hash_value), "Hash should contain only hexadecimal characters"
        
    def test_generate_random_hash_uniqueness(self):
        """Test that generated hashes are unique."""
        hashes = [generate_random_hash() for _ in range(10)]
        assert len(set(hashes)) == 10, "Generated hashes should be unique"
        
    def test_find_hash_with_prefix_success(self):
        """Test finding a hash with a common prefix that should succeed."""
        # Using a single character prefix to ensure the test reliably passes
        success, hash_value, attempts = find_hash_with_prefix("0", 100)
        
        assert success is True, "Should find a hash starting with '0'"
        assert hash_value.startswith("0"), f"Hash {hash_value} should start with '0'"
        assert 1 <= attempts <= 100, f"Attempts should be between 1 and 100, got {attempts}"
        
    def test_find_hash_with_prefix_failure(self):
        """Test finding a hash with a very unlikely prefix."""
        # Using a prefix that's extremely unlikely to be found in limited attempts
        success, hash_value, attempts = find_hash_with_prefix("000000000", 10)
        
        assert success is False, "Should not find such an unlikely hash prefix"
        assert hash_value is None, "Hash value should be None when not found"
        assert attempts == 10, f"Should have made exactly 10 attempts, got {attempts}"
        
    def test_find_hash_with_invalid_prefix_type(self):
        """Test error handling for invalid prefix type."""
        with pytest.raises(TypeError):
            find_hash_with_prefix(123, 100)
            
    def test_find_hash_with_invalid_max_attempts(self):
        """Test error handling for invalid max_attempts."""
        with pytest.raises(ValueError):
            find_hash_with_prefix("00", -1)
            
        with pytest.raises(ValueError):
            find_hash_with_prefix("00", 0)
            
    @patch('main.find_hash_with_prefix')
    def test_main_success(self, mock_find_hash):
        """Test main function when hash is found."""
        mock_find_hash.return_value = (True, "00abcdef", 42)
        
        result = main()
        
        assert result is True, "Main should return True when hash is found"
        mock_find_hash.assert_called_once_with("00", 1000)
        
    @patch('main.find_hash_with_prefix')
    def test_main_failure(self, mock_find_hash):
        """Test main function when hash is not found."""
        mock_find_hash.return_value = (False, None, 1000)
        
        result = main()
        
        assert result is False, "Main should return False when hash is not found"
        mock_find_hash.assert_called_once_with("00", 1000)
        
    @patch('main.find_hash_with_prefix')
    def test_main_exception_handling(self, mock_find_hash):
        """Test main function's exception handling."""
        mock_find_hash.side_effect = Exception("Test exception")
        
        result = main()
        
        assert result is False, "Main should return False when an exception occurs"


if __name__ == "__main__":
    pytest.main(["-v"])

