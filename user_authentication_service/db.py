#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add new user to the DB

        Args:
            email (str): User email
            hashed_password (str): hidden password

        Returns:
            User: Newly created user object
        """
        userObj = User(email=email, hashed_password=hashed_password)
        self._session.add(userObj)
        self._session.commit()
        self._session.refresh(userObj)
        return userObj

    def find_user_by(self, **kwargs) -> User:
        """Takes in keyword and returns first user filtered by keyword

        Returns:
            User: First user found from filtering
        """
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError

        sessionQuery = self._session.query(User).filter_by(**kwargs).first()
        if sessionQuery is None:
            raise NoResultFound
        return sessionQuery
