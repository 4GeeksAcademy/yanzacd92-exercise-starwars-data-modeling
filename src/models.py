import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    height = Column(Float)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    mass = Column(Float)
    name = Column(String(250), nullable=False)
    skin_color = Column(String(50))
    created = Column(DateTime)
    edited = Column(DateTime)

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    opening_crawl = Column(String(250))
    director = Column(String(100))
    producer = Column(String(100))
    release_date = Column(DateTime)
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)

class Startships(Base):
    __tablename__ = 'startships'
    id = Column(Integer, primary_key=True)
    name  = Column(String(250))
    model  = Column(String(250))
    starship_class  = Column(String(100))
    manufacturer  = Column(String(100))
    cost_in_credits  = Column(DateTime)
    length = Column(Float)
    crew = Column(Float)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(Float)
    mglt = Column(String(50))
    cargo_capacity = Column(Integer)
    consumables = Column(String(50))
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)

class Vehicles(Base):
    __tablename__ = 'vehicles'
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
    created = Column(DateTime)
    edited = Column(DateTime)

class Species(Base):
    __tablename__ = 'species'
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
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)

class Planets(Base):
    __tablename__ = 'planets'
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
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)

class Cast(Base):
    __tablename__ = 'cast'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship("Films", backref="cast")
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship("People", backref="cast")

class PeopleVehicles(Base):
    __tablename__ = 'peoplevehicles'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)

class PeopleSpecies(Base):
    __tablename__ = 'peoplespecies'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    species_id = Column(Integer, ForeignKey('species.id'), primary_key=True)

class PeopleFilms(Base):
    __tablename__ = 'peoplefilms'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    films_id = Column(Integer, ForeignKey('films.id'), primary_key=True)

class PeopleStarship(Base):
    __tablename__ = 'peoplestartship'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    startships_id = Column(Integer, ForeignKey('startships.id'), primary_key=True)

class FilmsPlanets(Base):
    __tablename__ = 'filmsplanets'
    films_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)

class FilmsSpecies(Base):
    __tablename__ = 'filmsspecies'
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    species_id = Column(Integer, ForeignKey('species.id'), primary_key=True)

class FilmsVehicles(Base):
    __tablename__ = 'filmsvehicles'
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)

class FilmsStartships(Base):
    __tablename__ = 'filmsstarships'
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    startships_id = Column(Integer, ForeignKey('startships.id'), primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
