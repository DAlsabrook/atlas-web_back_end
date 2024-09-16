#!/usr/bin/env python3
"""
idk what this does yet
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check is password matches the hashed password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
