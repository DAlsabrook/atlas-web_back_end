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
        if (path is None
                or excluded_paths is None
                or excluded_paths is ""):
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """No idea what this does either"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """And again... no idea what this does"""
        return None
