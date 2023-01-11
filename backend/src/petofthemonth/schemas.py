from typing import Union, Optional

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

class User(UserBase):
    id: int
    is_active: bool

class Group(GroupBase):
    id: int

class UserRead(User):
    id: int
    is_active: bool
    groups: list[Group] = []
    pets: list[Pet] = []

class GroupRead(Group):
    id: int
    pets: list[Pet] = []
    users: list[User] = []

class PetRead(Pet):
    id: int
    points: list[Point] = []
    groups: list[Group] = []
    users: list[User] = []