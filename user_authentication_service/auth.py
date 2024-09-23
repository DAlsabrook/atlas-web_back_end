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

    def create_session(self, email: str) -> str:
        """Takes emaiul and returns session id

        Args:
            email (str): user email

        Returns:
            str: Session id user is attached to
        """
        user = self._db.find_user_by(email=email)
        userNewSessionId = _generate_uuid()
        self._db.update_user(user.id, session_id=userNewSessionId)
        return userNewSessionId

    def get_user_from_session_id(self, session_id: str) -> User:
        """_summary_

        Args:
            session_id (str): _description_

        Returns:
            User: _description_
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """_summary_

        Args:
            user_id (str): _description_
        """
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """get reset token

        Args:
            email (str): User email

        Returns:
            str: UUID reset token
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using the reset token

        Args:
            reset_token (str): Reset token to identify the user
            password (str): New password to set

        Raises:
            ValueError: If the reset token is invalid
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        new_hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=new_hashed_password,
                             reset_token=None)


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation.

    Returns:
        str: The string representation of the new UUID.
    """
    import uuid
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """Hash the password and return the bytes from the hash

    Args:
        password (str): Password to hash
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
