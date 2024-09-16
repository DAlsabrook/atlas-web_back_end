#!/usr/bin/env python3
"""
Module to handle function for authorization
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Class to handle auth
    """

    def __init__(self):
        """Initialize auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """No idea what this does"""
        return False

    def authorization_header(self, request=None) -> str:
        """No idea what this does either"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """And again... no idea what this does"""
        return None
