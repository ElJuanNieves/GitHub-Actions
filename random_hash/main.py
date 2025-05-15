#!/usr/bin/env python3
"""
Random Hash Generator

This script generates random 32-character SHA256 hashes and checks
if any of them start with two consecutive zeros ('00').
It will make up to 1000 attempts to find such a hash.
"""

import hashlib
import os
from typing import Tuple, Optional


def generate_random_hash() -> str:
    """
    Generate a random 32-character hexadecimal hash using SHA256.
    
    Returns:
        str: A 32-character hexadecimal hash
    """
    # Generate 16 bytes of random data (which will result in a 32-character hex hash)
    random_bytes = os.urandom(16)
    
    # Create SHA256 hash of the random bytes
    hash_obj = hashlib.sha256(random_bytes)
    
    # Return the hexadecimal digest
    return hash_obj.hexdigest()


def find_hash_with_prefix(prefix: str = "00", max_attempts: int = 1000) -> Tuple[bool, Optional[str], int]:
    """
    Try to find a hash that starts with the specified prefix within a maximum number of attempts.
    
    Args:
        prefix (str): The prefix to search for at the start of hashes
        max_attempts (int): Maximum number of attempts to make
        
    Returns:
        Tuple[bool, Optional[str], int]: 
            - Success status (True if found, False if not)
            - The hash that matches the criteria (None if not found)
            - The number of attempts made
    """
    if not isinstance(prefix, str):
        raise TypeError("Prefix must be a string")
    
    if not isinstance(max_attempts, int) or max_attempts <= 0:
        raise ValueError("Max attempts must be a positive integer")
        
    for attempt in range(1, max_attempts + 1):
        current_hash = generate_random_hash()
        
        if current_hash.startswith(prefix):
            return True, current_hash, attempt
            
    return False, None, max_attempts


def main() -> bool:
    """
    Main function to find a hash starting with '00' in at most 1000 attempts.
    
    Returns:
        bool: True if a matching hash was found, False otherwise
    """
    try:
        success, hash_value, attempts = find_hash_with_prefix("00", 1000)
        
        if success:
            print(f"Success! Found hash starting with '00' after {attempts} attempts:")
            print(f"Hash: {hash_value}")
        else:
            print(f"Failed to find a hash starting with '00' after {attempts} attempts.")
            
        return success
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    main()

