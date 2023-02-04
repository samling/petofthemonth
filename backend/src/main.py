import logging
import uvicorn

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM
from src.routes import users, groups, pets, points

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(users.router)
app.include_router(groups.router)
app.include_router(pets.router)
app.include_router(points.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello world"