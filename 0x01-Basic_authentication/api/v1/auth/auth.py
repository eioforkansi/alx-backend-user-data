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
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths that don't require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if path is None or not excluded_paths:
            return True

        processed_path = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            processed_excluded_path = excluded_path.rstrip('/') + '/'
            if processed_path == processed_excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the Authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            The value of the Authorization header, or None if not present.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user associated with a request.
        """
        return None
