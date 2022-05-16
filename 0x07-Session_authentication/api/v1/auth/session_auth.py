#!/usr/bin/env python3
"""
session authentication moduel
"""
from ast import Not
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create Session ID For User_id
        """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            sessionID = str(uuid4())
            self.user_id_by_session_id = {sessionID: user_id}
            return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id is None or type(session_id) is not str:
            return None
        else:
            return self.user_id_by_session_id.get(session_id)
