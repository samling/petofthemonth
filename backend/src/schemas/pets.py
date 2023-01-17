from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Pets

Tortoise.init_models(["src.database.models"], "models")

PetInSchema = pydantic_model_creator(
    Pets, name="PetIn", exclude_readonly=True
)

PetOutSchema = pydantic_model_creator(
    Pets, name="PetOut", exclude=[
        "created_at",
        "modified_at",
        "users.created_at",
        "users.modified_at",
        "users.password",
        "groups.users"
    ]
)

class UpdatePet(BaseModel):
    name: Optional[str]
    description: Optional[str]
    age: Optional[int]
    height: Optional[int]
    weight: Optional[int]
    dob: Optional[datetime]