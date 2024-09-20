#!/usr/bin/env python3
"""
Module to handle auth to get things from the DB
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash the password and return the bytes from the hash

    Args:
        password (str): Password to hash
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
