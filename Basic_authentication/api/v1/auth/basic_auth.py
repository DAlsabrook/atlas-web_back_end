#!/usr/bin/env python3
"""module for base authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class that contains the basic authentication methods"""

    def __init__(self):
        """initialize basic auth"""
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns base64 part of the request header
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith('Basic'):
            tokenized = authorization_header.split(' ')
            if tokenized[1]:
                return tokenized[1]
        return None
