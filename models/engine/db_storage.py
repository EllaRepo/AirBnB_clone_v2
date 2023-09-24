#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages db storage of hbnb models
    Attributes:
        engine : private class attribute
        session : private class attribute
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization
        """
        usr = getenv('HBNB_MYSQL_USER')
        paswd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(usr, paswd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query on the current database session
        Return:
            returns a dictionary of __object
        """
        dic = {}
        classes = classes = [State, City, Place, User, Amenity, Review] \
            if cls is None else [eval(cls) if type(cls) == str else cls]
        for c in classes:
            for elem in self.__session.query(c):
                dic["{}.{}".format(type(elem).__name__, elem.id)] = elem
        return (dic)

    def new(self, obj):
        """Adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        sessn = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessn)
        self.__session = Session()

    def close(self):
        """Call remove method on session
        """
        self.__session.close()
