from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Points
from src.schemas.points import PointOutSchema
from src.schemas.token import Status

async def get_points():
    return await PointOutSchema.from_queryset(Points.all())

async def get_point(point_id) -> PointOutSchema:
    return await PointOutSchema.from_queryset_single(Points.get(id=point_id))

async def create_point(point, current_user) -> PointOutSchema:
    point_dict = point.dict(exclude_unset=True)
    point_obj = await Points.create(**point_dict)
    return await PointOutSchema.from_tortoise_orm(point_obj)

async def update_point(point_id, point, current_user) -> PointOutSchema:
    try:
        db_point = await PointOutSchema.from_queryset_single(Points.get(id=point_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Point {point_id} not found")
    
    #TODO: Check that the current user is in owner list
    await Points.filter(id=point_id).update(**point.dict(exclude_unset=True))
    return await PointOutSchema.from_queryset_single(Points.get(id=point_id))

    #TODO: Return exception if not in owner list

async def delete_point(point_id, current_user) -> Status:
    try:
        db_point = await PointOutSchema.from_queryset_single(Points.get(id=point_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Point {point_id} not found")

    #TODO: Check that the current user is in owner list
    deleted_count = await Points.filter(id=point_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Point {point_id} not found")
    return Status(message=f"Deleted point {point_id}")

    #TODO: Return exception if not in owner list
