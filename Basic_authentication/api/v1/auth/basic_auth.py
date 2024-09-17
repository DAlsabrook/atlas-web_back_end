#!/usr/bin/env python3
"""module for base authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class that contains the basic authentication methods"""

    def __init__(self):
        """initialize basic auth"""
        super().__init__()


