from tortoise import Tortoise

Tortoise.init_models(["src.database.models"], "models")