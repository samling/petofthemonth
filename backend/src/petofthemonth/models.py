from typing import TypedDict
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship

from .database import Base

user_groups = Table('user_groups', Base.metadata, \
    Column('user_id', ForeignKey('users.id'), primary_key=True), \
    Column('group_id', ForeignKey('groups.id'), primary_key=True)
)

user_pets = Table('user_pets', Base.metadata, \
    Column('user_id', ForeignKey('users.id'), primary_key=True), \
    Column('pet_id', ForeignKey('pets.id'), primary_key=True)
)

group_pets = Table('group_pets', Base.metadata, \
    Column('group_id', ForeignKey('groups.id'), primary_key=True), \
    Column('pet_id', ForeignKey('pets.id'), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    is_active = Column(Boolean, default=True)

    groups = relationship("Group", secondary='user_groups', back_populates="users")

    pets = relationship("Pet", secondary='user_pets', back_populates="users")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_date = Column(DateTime)
    description = Column(String)

    users = relationship("User", secondary='user_groups', back_populates="groups")

    pets = relationship("Pet", secondary='group_pets', back_populates="groups")

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    name = Column(String, unique=False, index=True)
    age = Column(Integer)
    dob = Column(DateTime)
    height = Column(Integer)
    weight = Column(Integer)
    description = Column(String)

    points = relationship("Point", back_populates="pet")
    groups = relationship("Group", secondary='group_pets', back_populates="pets")
    users = relationship("User", secondary='user_pets', back_populates="pets")

class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime)
    description = Column(String)
    pet_id = Column(Integer, ForeignKey("pets.id"))

    pet = relationship("Pet", back_populates="points")