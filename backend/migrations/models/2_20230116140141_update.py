from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "groupuser" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "group_id" INT NOT NULL REFERENCES "groups" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);;
        CREATE TABLE "groupuser" (
    "groups_id" INT NOT NULL REFERENCES "groups" ("id") ON DELETE CASCADE,
    "users_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "groupuser";
        DROP TABLE IF EXISTS "groupuser";"""
