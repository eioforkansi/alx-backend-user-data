#!/usr/bin/env python3
"""
API authentication Module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template for authentication systems."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from a Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user associated with a request.
        """
        return None
