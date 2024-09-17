#!/usr/bin/env python3
"""module for base authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Class that contains the basic authentication methods"""

    def __init__(self):
        """initialize basic auth"""
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns base64 part of the request header
        """
        if (authorization_header is None or not isinstance(
                authorization_header, str
                )):
            return None
        if authorization_header.startswith('Basic'):
            tokenized = authorization_header.split(' ')
            if tokenized[1]:
                return tokenized[1]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns base64 part of the request header
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str
                ):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> tuple[str, str]:
        """returns base64 part of the request header
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str
                ):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        tokenized = decoded_base64_authorization_header.split(':')
        return (tokenized[0], tokenized[1])
