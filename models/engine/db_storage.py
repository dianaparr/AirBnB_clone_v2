#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy import scope_session
from sqlalchemy.orm import sessionmakers
# from sqlalchemy import orm
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """ Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv(
                'HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            cls_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            new_dict = {}
            for class_name in cls_list:
                query = self.__session.query(class_name).all()
            print("Hola")

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = orm.scope_session(session_fact)
        self.__session = Session()
