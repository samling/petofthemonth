from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Users

Tortoise.init_models(["src.database.models"], "models")

UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)

UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)