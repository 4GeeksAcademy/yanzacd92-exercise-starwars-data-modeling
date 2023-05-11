import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table people
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(50))
    eye_color = Column(String(50))
    # film_id = Column(Integer, ForeignKey('films.id'))
    gender = Column(String(50))
    hair_color = Column(String(50))
    height = Column(Float)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    mass = Column(Float)
    name = Column(String(250), nullable=False)
    skin_color = Column(String(50))
    created = Column(DateTime)
    edited = Column(DateTime)
    # specie_id = Column(Integer, ForeignKey('species.id'))
    # vehicle_id = Column(Integer, ForeignKey('vehicles.id'))

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table films
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    opening_crawl = Column(String(250))
    director = Column(String(100))
    producer = Column(String(100))
    release_date = Column(DateTime)
    # specie_id = Column(Integer, ForeignKey('species.id'))
    # vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    # character_id = Column(Integer, ForeignKey('people.id'))
    # planet_id = Column(Integer, ForeignKey('planets.id'))
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table vehicles
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    model = Column(String(50))
    vehicle_class = Column(String(50))
    manufacturer = Column(String(100))
    length = Column(Float)
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(200))
    url = Column(String(250))
    # film_id = Column(Integer, ForeignKey('films.id'))
    # pilot_id = Column(Integer, ForeignKey('people.id'))
    created = Column(DateTime)
    edited = Column(DateTime)

class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table species
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    classification = Column(String(50))
    designation = Column(String(100))
    average_height = Column(Float)
    average_lifespan = Column(Float)
    eye_colors = Column(String(50))
    hair_colors = Column(String(50))
    skin_colors = Column(String(50))
    language = Column(String(50))
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    # character_id = Column(Integer, ForeignKey('people.id'))
    # film_id = Column(Integer, ForeignKey('films.id'))
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Float)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Float)
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    residents_id = Column(Integer, ForeignKey('people.id'))
    # film_id = Column(Integer, ForeignKey('films.id'))
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)

class PeopleVehicles(Base):
    __tablename__ = 'peoplevehicles'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)

class PeopleSpecies(Base):
    __tablename__ = 'peoplespecies'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    specie_id = Column(Integer, ForeignKey('species.id'), primary_key=True)

class PeopleFilms(Base):
    __tablename__ = 'peoplefilms'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)

class FilmsPlanets(Base):
    __tablename__ = 'filmsplanets'
    people_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)

class FilmsSpecies(Base):
    __tablename__ = 'filmsspecies'
    people_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('species.id'), primary_key=True)

class FilmsVehicles(Base):
    __tablename__ = 'filmsvehicles'
    people_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
