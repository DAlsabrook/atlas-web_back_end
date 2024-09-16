#!/usr/bin/env python3
"""
idk what this does yet
"""
import bcrypt


def hash_password(password):
    """returns a hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
