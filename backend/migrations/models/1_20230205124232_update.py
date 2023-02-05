from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "petimages" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "filename" TEXT NOT NULL,
    "pet_id" INT NOT NULL REFERENCES "pets" ("id") ON DELETE CASCADE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "petimages";"""
