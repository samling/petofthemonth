from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.pets as crud
from src.auth.jwthandler import get_current_user
from src.schemas.pets import PetInSchema, PetOutSchema, UpdatePet
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

router = APIRouter()

@router.get(
    "/pets",
    response_model=List[PetOutSchema],
    dependencies=[Depends(get_current_user)]
)
async def get_pets():
    return await crud.get_pets()

@router.get(
    "/pet/{pet_id}",
    response_model=PetOutSchema,
    dependencies=[Depends(get_current_user)]
)
async def get_pet(
    pet_id: int
) -> PetOutSchema:
    try:
        return await crud.get_pet(pet_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pet does not exist"
        )

@router.post(
    "/pets", response_model=PetOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_pet(
    pet: PetInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> PetOutSchema:
    return await crud.create_pet(pet, current_user)

@router.patch(
    "/pet/{pet_id}",
    dependencies=[Depends(get_current_user)],
    response_model=PetOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_pet(
    pet_id: int,
    pet: UpdatePet,
    current_user: UserOutSchema = Depends(get_current_user)
) -> PetOutSchema:
    return await crud.update_pet(pet_id, pet, current_user)

@router.delete(
    "/pet/{pet_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)]
)
async def delete_pet(
    pet_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_pet(pet_id, current_user)