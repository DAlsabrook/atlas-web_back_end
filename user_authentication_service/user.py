#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String


class User():
    """User class for the user table

    Returns:
        str: string representation of the user
    """
    __table__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
           self.name, self.fullname, self.nickname)
