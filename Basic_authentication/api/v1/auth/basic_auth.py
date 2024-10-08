#!/usr/bin/env python3
"""module for base authentication
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """Used to get the user obj from credentials
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
            if user and user[0]:
                if user[0].is_valid_password(user_pwd):
                    return user[0]
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that overloads Auth class and retrieves User"""
        if request is None:
            return None

        auth = self.authorization_header(request)
        if auth is None:
            return None

        base64Auth = self.extract_base64_authorization_header(auth)
        if base64Auth is None:
            return None

        decodedAuth = self.decode_base64_authorization_header(base64Auth)
        if decodedAuth is None:
            return None

        userCred = self.extract_user_credentials(decodedAuth)
        if userCred[0] is None or userCred[1] is None:
            return None

        userObj = self.user_object_from_credentials(userCred[0], userCred[1])
        if userObj is None:
            return None

        return userObj
