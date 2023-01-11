from datetime import timedelta

from fastapi import APIRouter, Depends, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from . import crud, schemas
from .auth.users import validate_user
from .auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from sqlalchemy.orm import Session

router = APIRouter()

def get_db(request: Request):
    return request.state.db

@router.get("/")
def read_root():
    return "Hello world"

@router.post("/register", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = validate_user(db=db, user=user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in."}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False
    )

    return response

@router.get("/users/whoami", response_model=schemas.UserRead, dependencies=[Depends(get_current_user)])
async def read_users_me(current_user: schemas.UserRead = Depends(get_current_user)):
    return current_user

@router.delete(
    "/user/{user_id}",
    response_model=schemas.Status,
    responses={404: {"msg": "Model not found"}},
    dependencies=[Depends(get_current_user)]
)
async def delete_user(
    user_id: int, current_user: schemas.UserRead = Depends(get_current_user), db: Session = Depends(get_db)
) -> schemas.Status:
    return await crud.delete_user(db, user_id=user_id)

# Users
@router.get("/users/", response_model=list[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.post("/users/{user_id}/pets/", response_model=schemas.Pet)
def create_pet_for_user(user_id: int, pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return crud.create_user_pet(db=db, pet=pet, user_id=user_id)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    response = crud.delete_user(db, user_id=user_id)
    return response


# Groups
@router.get("/groups/", response_model=list[schemas.GroupRead])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = crud.get_groups(db, skip=skip, limit=limit)
    return groups

@router.get("/groups/{group_id}", response_model=schemas.GroupRead)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@router.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)

@router.patch("/groups/{group_id}/users/{user_id}", response_model=schemas.Group)
def update_group_users(group_id: int, user_id: int, db: Session = Depends(get_db)):
    return crud.update_group_users(db, group_id=group_id, user_id=user_id)

@router.patch("/groups/{group_id}/pets/{pet_id}", response_model=schemas.Group)
def update_group_pets(group_id: int, pet_id: int, db: Session = Depends(get_db)):
    return crud.update_group_pets(db, group_id=group_id, pet_id=pet_id)

@router.delete("/groups/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    response = crud.delete_group(db, group_id=group_id)
    return response


# Pets
@router.get("/pets/", response_model=list[schemas.PetRead])
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pets = crud.get_pets(db, skip=skip, limit=limit)
    return pets

@router.get("/pets/{pet_id}", response_model=schemas.PetRead)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = crud.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

@router.post("/pets/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db=db, pet=pet)

@router.patch("/pets/{pet_id}/users/{user_id}", response_model=schemas.Pet)
def update_pet_users(pet_id: int, user_id: int, db: Session = Depends(get_db)):
    return crud.update_pet_users(db, pet_id=pet_id, user_id=user_id)

@router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    response = crud.delete_pet(db, pet_id=pet_id)
    return response


# Points
@router.get("/points/", response_model=list[schemas.Point])
def read_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    points = crud.get_points(db, skip=skip, limit=limit)
    return points

@router.get("/points/{point_id}", response_model=schemas.Point)
def read_point(point_id: int, db: Session = Depends(get_db)):
    db_point = crud.get_point(db, point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point

@router.post("/pets/{pet_id}/points/", response_model=schemas.Point)
def create_point_for_pet(pet_id: int, point: schemas.PointCreate, db: Session = Depends(get_db)):
    return crud.create_pet_point(db=db, point=point, pet_id=pet_id)

@router.delete("/points/{point_id}")
def delete_point(point_id: int, db: Session = Depends(get_db)):
    response = crud.delete_point(db, point_id=point_id)
    return response