from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.groups as crud
from src.auth.jwthandler import get_current_user
from src.schemas.groups import GroupInSchema, GroupOutSchema, UpdateGroup
from src.schemas.pets import PetInSchema, PetOutSchema, UpdatePet
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

router = APIRouter()

@router.get(
    "/groups",
    response_model=List[GroupOutSchema],
    dependencies=[Depends(get_current_user)]
)
async def get_groups():
    return await crud.get_groups()

@router.get(
    "/group/{group_id}",
    response_model=GroupOutSchema,
    dependencies=[Depends(get_current_user)]
)
async def get_group(
    group_id: int
) -> GroupOutSchema:
    try:
        return await crud.get_group(group_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Group does not exist"
        )

@router.post(
    "/groups", response_model=GroupOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_group(
    group: GroupInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> GroupOutSchema:
    return await crud.create_group(group, current_user)

@router.patch(
    "/group/{group_id}/pets/{pet_id}",
    dependencies=[Depends(get_current_user)],
    response_model=GroupOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_group_pets(
    group_id: int,
    group: UpdateGroup,
    pet_id: int,
    current_user: UserOutSchema = Depends(get_current_user)
) -> GroupOutSchema:
    return await crud.update_group_pets(group_id, group, pet_id, current_user)

@router.patch(
    "/group/{group_id}",
    dependencies=[Depends(get_current_user)],
    response_model=GroupOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_group(
    group_id: int,
    group: UpdateGroup,
    current_user: UserOutSchema = Depends(get_current_user)
) -> GroupOutSchema:
    return await crud.update_group(group_id, group, current_user)

@router.delete(
    "/group/{group_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)]
)
async def delete_group(
    group_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_group(group_id, current_user)