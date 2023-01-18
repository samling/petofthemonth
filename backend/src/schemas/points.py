from typing import Optional
from pydantic import BaseModel

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Points

PointInSchema = pydantic_model_creator(
    Points, name="PointIn", exclude=["pet_id"], exclude_readonly=True
)

PointOutSchema = pydantic_model_creator(
    Points, name="PointOut", exclude=[
        "modified_at",
        "pet.created_at",
        "pet.modified_at",
        "pet.groups",
        "pet.users",
    ]
)

class UpdatePoint(BaseModel):
    description: Optional[str]