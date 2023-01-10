from typing import Union

from datetime import datetime

from pydantic import BaseModel

class PointBase(BaseModel):
    created_date: datetime
    description: Union[str, None] = None

    class Config:
        orm_mode = True

class PetBase(BaseModel):
    name: str
    created_date: datetime
    age: int
    dob: datetime
    height: int
    weight: int
    description: Union[str, None] = None

    class Config:
        orm_mode = True

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

class PointCreate(PointBase):
    pass

class PetCreate(PetBase):
    pass

class UserCreate(UserBase):
    password: str

class GroupCreate(GroupBase):
    pass

class Point(PointBase):
    id: int
    pet_id: int

class Pet(PetBase):
    id: int
    points: list[PointBase] = []
    groups: list[GroupBase] = []
    owners: list[UserBase] = []

class User(UserBase):
    id: int
    is_active: bool
    groups: list[GroupBase] = []
    pets: list[PetBase] = []

class Group(GroupBase):
    id: int
    pets: list[PetBase] = []
    users: list[UserBase] = []