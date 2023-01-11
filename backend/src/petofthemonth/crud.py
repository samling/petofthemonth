from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session, joinedload

from . import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Users
def get_user(db: Session, user_id: int):
    return db.query(models.User).options(joinedload(models.User.groups), joinedload(models.User.pets)).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).options(joinedload(models.User.groups), joinedload(models.User.pets)).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: int):
    return db.query(models.User).options(joinedload(models.User.groups), joinedload(models.User.pets)).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).options(joinedload(models.User.groups), joinedload(models.User.pets)).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    user.password = pwd_context.encrypt(user.password)
    db_user = models.User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=user.password,
        created_date=user.created_date,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    db.delete(db_user)
    db.commit()

    return { "ok": True }

# Groups
def get_group(db: Session, group_id: int):
    return db.query(models.Group).options(joinedload(models.Group.users), joinedload(models.Group.pets)).filter(models.Group.id == group_id).first()

def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).options(joinedload(models.Group.users), joinedload(models.Group.pets)).offset(skip).limit(limit).all()

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def update_group_users(db: Session, group_id: int, user_id: int):
    db_group = get_group(db, group_id=group_id)
    db_user = get_user(db, user_id=user_id)
    db_group.users.append(db_user)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group

def update_group_pets(db: Session, group_id: int, pet_id: int):
    db_group = get_group(db, group_id=group_id)
    pet = get_pet(db, pet_id=pet_id)
    db_group.pets.append(pet) 
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group

def delete_group(db: Session, group_id: int):
    db_group = get_group(db, group_id)
    db.delete(db_group)
    db.commit()

    return { "ok": True }

# Pets
def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).options(joinedload(models.Pet.users), joinedload(models.Pet.groups)).filter(models.Pet.id == pet_id).first()

def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pet).options(joinedload(models.Pet.users), joinedload(models.Pet.groups)).offset(skip).limit(limit).all()

def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def create_user_pet(db: Session, pet: schemas.PetCreate, user_id: int):
    user = get_user(db, user_id)
    db_pet = models.Pet(**pet.dict(), users=[user])
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def update_pet_users(db: Session, pet_id: int, user_id: int):
    db_pet = get_pet(db, pet_id=pet_id)
    user = get_user(db, user_id=user_id)
    db_pet.users.append(user)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)

    return db_pet

def delete_pet(db: Session, pet_id: int):
    db_pet = get_pet(db, pet_id)
    db.delete(db_pet)
    db.commit()

    return { "ok": True }

# Points
def get_point(db: Session, point_id: int):
    return db.query(models.Point).filter(models.Point.id == point_id).first()

def get_points(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Point).offset(skip).limit(limit).all()

def create_pet_point(db: Session, point: schemas.PointCreate, pet_id: int):
    db_point = models.Point(**point.dict(), pet_id=pet_id)
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

def delete_point(db: Session, point_id: int):
    db_point = get_point(db, point_id)
    db.delete(db_point)
    db.commit()

    return { "ok": True }
