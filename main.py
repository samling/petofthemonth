import logging
import uvicorn

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

from src.petofthemonth import crud, models, schemas
from src.petofthemonth.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

def get_db(request: Request):
    return request.state.db

@app.get("/")
def read_root():
    return "Hello world"

# Users
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

# Groups
@app.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)

@app.patch("/groups/{group_id}/users/{user_id}", response_model=schemas.Group)
def update_group_users(group_id: int, user_id: int, db: Session = Depends(get_db)):
    group = crud.get_group(db, group_id=group_id)
    user = crud.get_user(db, user_id=user_id)
    group.users.append(user)
    db.add(group)
    db.commit()
    db.refresh(group)

    return group

@app.get("/groups/", response_model=list[schemas.Group])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = crud.get_groups(db, skip=skip, limit=limit)
    return groups

@app.get("/groups/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="group not found")
    return db_group

# Pets
@app.post("/groups/{group_id}/pets/", response_model=schemas.Pet)
def create_pet_for_group(group_id: int, pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return crud.create_group_pet(db=db, pet=pet, group_id=group_id)

@app.get("/pets/", response_model=list[schemas.Pet])
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pets = crud.get_pets(db, skip=skip, limit=limit)
    return pets

@app.get("/pets/{pet_id}", response_model=schemas.Pet)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = crud.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

# Points
@app.post("/pets/{pet_id}/points/", response_model=schemas.Point)
def create_point_for_pet(pet_id: int, point: schemas.PointCreate, db: Session = Depends(get_db)):
    return crud.create_pet_point(db=db, point=point, pet_id=pet_id)

@app.get("/points/", response_model=list[schemas.Point])
def read_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    points = crud.get_points(db, skip=skip, limit=limit)
    return points

@app.get("/points/{point_id}", response_model=schemas.Point)
def read_point(point_id: int, db: Session = Depends(get_db)):
    db_point = crud.get_point(db, point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
