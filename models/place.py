#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', cascade="all, delete", backref='place')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """
            getter attribute cities that returns the list of Review instances
            with state_id equals to the current Place.id
            """
            from models.review import Review
            from models import storage
            new_list = []
            for key, value in storage.all(Review).items():
                if self.id == value.place_id:
                    new_list.append(value)
            return new_list

        @property
        def amenities(self):
            """
            getter attribute cities that returns the list of Review instances
            with state_id equals to the current Place.id
            """
            from models.amenity import Amenity
            from models import storage
            new_list = []
            for key, value in storage.all(Amenity).items():
                if self.id == value.id:
                    new_list.append(value)
            return new_list

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity

            if value.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(value.id)
