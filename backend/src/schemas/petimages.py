from typing import Optional
from pydantic import BaseModel

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import PetImages

PetImageInSchema = pydantic_model_creator(
    PetImages, name="PetImageIn", exclude=["pet_id"], exclude_readonly=True
)

PetImageOutSchema = pydantic_model_creator(
    PetImages, name="PetImageOut", exclude=[
        "modified_at",
        "pet.created_at",
        "pet.modified_at",
        "pet.groups",
        "pet.users.password",
    ]
)

class UpdatePetImage(BaseModel):
    filename: Optional[str]