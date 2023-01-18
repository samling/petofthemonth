from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Groups

GroupInSchema = pydantic_model_creator(
    Groups, name="GroupIn", exclude_readonly=True
)

GroupOutSchema = pydantic_model_creator(
    Groups, name="GroupOut", exclude=[
        "created_at",
        "modified_at",
        "users.created_at",
        "users.modified_at",
        "users.password",
        "pets.users.password"
    ]
)

class UpdateGroup(BaseModel):
    name: Optional[str]
    description: Optional[str]