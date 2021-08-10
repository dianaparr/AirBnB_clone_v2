#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from sqlalchemy import (create_engine)
from os import getenv
from models.base_model import Base

class DBStorage():
    """ Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        Session = sessionmaker(bind=self.__engine)
        # create a Session
        __session = Session()
        if cls is None:
            class_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            new_dict = {}
            for class_name in class_list:
                query = __session.query(class_name).all()
                for record in query:
                    print("Hola")


        if cls is None:
            return FileStorage.__objects
        else:
            new_dict = {}
            for obj, value in FileStorage.__objects.items():
                if cls.__name__ == value.__class__.__name__:
                    new_dict[obj] = FileStorage.__objects[obj]
            return new_dict
