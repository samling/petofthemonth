import os

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URI")},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}