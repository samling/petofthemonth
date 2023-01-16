from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "groups" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "description" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "pets" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "description" TEXT NOT NULL,
    "age" INT NOT NULL,
    "height" INT NOT NULL,
    "weight" INT NOT NULL,
    "dob" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "points" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "description" TEXT NOT NULL,
    "pet_id" INT NOT NULL REFERENCES "pets" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "email" VARCHAR(50) NOT NULL UNIQUE,
    "fullname" VARCHAR(50),
    "password" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT True
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
