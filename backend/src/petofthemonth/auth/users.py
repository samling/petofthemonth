from fastapi import HTTPException, Depends, status, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from src.petofthemonth.models import User
from src.petofthemonth.crud import get_user, get_user_by_username, get_user_by_email

from sqlalchemy.orm import Session


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, username: str):
    return get_user_by_username(db=db, username=username)


def validate_user(db: Session, user: OAuth2PasswordRequestForm = Depends()):
    db_user = get_user(db=db, username=user.username)

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    return db_user