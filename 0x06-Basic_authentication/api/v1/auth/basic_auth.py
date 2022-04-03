#!/usr/bin/env python3
"""
basic auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        """
        if authorization_header is None:
            return None
        elif isinstance(authorization_header, str) is False:
            return None
        elif authorization_header[0:6] != "Basic ":
            return None
        else:
            return authorization_header[6:]
