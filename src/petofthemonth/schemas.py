from typing import Union

from datetime import datetime

from pydantic import BaseModel

# Points
class PointBase(BaseModel):
    created_date: datetime
    description: Union[str, None] = None

class PointCreate(PointBase):
    pass

class Point(PointBase):
    id: int
    pet_id: int

    class Config:
        orm_mode = True

# Pets
class PetBase(BaseModel):
    name: str
    created_date: datetime
    age: int
    dob: datetime
    height: int
    weight: int
    description: Union[str, None] = None

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int
    points: list[Point] = []

    class Config:
        orm_mode = True

# Users and Groups
class UserBase(BaseModel):
    name: str
    created_date: datetime
    email: str
    description: Union[str, None] = None

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str
    created_date: datetime
    description: Union[str, None] = None

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class GroupCreate(GroupBase):
    pass

class User(UserBase):
    id: int
    is_active: bool
    groups: list[GroupBase] = []

class Group(GroupBase):
    id: int
    pets: list[Pet] = []
    users: list[UserBase] = []