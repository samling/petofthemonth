from sqlalchemy.orm import Session, joinedload

from . import models, schemas

# Users
def get_user(db: Session, user_id: int):
    return db.query(models.User).options(joinedload(models.User.groups)).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: int):
    return db.query(models.User).options(joinedload(models.User.groups)).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).options(joinedload(models.User.groups)).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password + "somehash"
    db_user = models.User(
        name=user.name,
        email=user.email,
        created_date=user.created_date,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Groups
def get_group(db: Session, group_id: int):
    return db.query(models.Group).options(joinedload(models.Group.users)).filter(models.Group.id == group_id).first()

def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).options(joinedload(models.Group.users)).offset(skip).limit(limit).all()

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

# Pets
def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()

def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pet).offset(skip).limit(limit).all()

def create_group_pet(db: Session, pet: schemas.PetCreate, group_id: int):
    db_pet = models.Pet(**pet.dict(), group_id=group_id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

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

