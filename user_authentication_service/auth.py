#!/usr/bin/env python3
"""
Module to handle auth to get things from the DB
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user to the db

        Args:
            email (str): user email
            password (str): user password

        Returns:
            User: user object
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pass = _hash_password(password)
            user = self._db.add_user(email, hashed_pass)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Check user in the session

        Args:
            email (str): user email to check
            password (str): user password to check

        Returns:
            bool: True if found
        """
        try:
            user = self._db.find_user_by(email=email)
            bytes_pass = password.encode('utf-8')
            hashed_pass = user.hashed_password
            return bcrypt.checkpw(bytes_pass, hashed_pass)
        except NoResultFound:
            return False


def _hash_password(password: str) -> bytes:
    """Hash the password and return the bytes from the hash

    Args:
        password (str): Password to hash
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
