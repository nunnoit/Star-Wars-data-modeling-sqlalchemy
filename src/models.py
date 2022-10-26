import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Person Table
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

# Address table
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

# Characters Table
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color  = Column(String(250))
    skin_color  = Column(String(250))
    eye_color  = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    homeworld = Column(String(250))

# Planets Table
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)

# Vehicles Table
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))


## Render Draw (SQLAlchemy base_
render_er(Base, 'diagram.png')