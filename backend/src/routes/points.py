from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.points as crud
from src.auth.jwthandler import get_current_user
from src.schemas.points import PointInSchema, PointOutSchema, UpdatePoint
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

router = APIRouter()

# exclude_user_password_pattern = {
#         "pet": {
#             "groups": {
#                 "__all__": {
#                     "users": {
#                         "__all__": {"password"}
#                     }
#                 }
#             }
#         }
#     }

@router.get(
    "/points",
    response_model=List[PointOutSchema],
    # response_model_exclude=exclude_user_password_pattern,
    dependencies=[Depends(get_current_user)]
)
async def get_points():
    return await crud.get_points()

@router.get(
    "/point/{point_id}",
    response_model=PointOutSchema,
    # response_model_exclude=exclude_user_password_pattern,
    dependencies=[Depends(get_current_user)]
)
async def get_point(
    point_id: int
) -> PointOutSchema:
    try:
        return await crud.get_point(point_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Point does not exist"
        )

@router.post(
    "/points",
    response_model=PointOutSchema,
    # response_model_exclude=exclude_user_password_pattern,
    dependencies=[Depends(get_current_user)]
)
async def create_point(
    point: PointInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> PointOutSchema:
    return await crud.create_point(point, current_user)

@router.patch(
    "/point/{point_id}",
    dependencies=[Depends(get_current_user)],
    response_model=PointOutSchema,
    # response_model_exclude=exclude_user_password_pattern,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_point(
    point_id: int,
    point: UpdatePoint,
    current_user: UserOutSchema = Depends(get_current_user)
) -> PointOutSchema:
    return await crud.update_point(point_id, point, current_user)

@router.delete(
    "/point/{point_id}",
    response_model=Status,
    # response_model_exclude=exclude_user_password_pattern,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)]
)
async def delete_point(
    point_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_point(point_id, current_user)