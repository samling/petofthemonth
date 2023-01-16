from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Groups
from src.schemas.groups import GroupOutSchema
from src.schemas.token import Status

async def get_groups():
    return await GroupOutSchema.from_queryset(Groups.all())

async def get_group(group_id) -> GroupOutSchema:
    return await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))

async def create_group(group, current_user) -> GroupOutSchema:
    group_dict = group.dict(exclude_unset=True)
    group_obj = await Groups.create(**group_dict)
    return await GroupOutSchema.from_tortoise_orm(group_obj)

async def update_group(group_id, group, current_user) -> GroupOutSchema:
    try:
        db_group = await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Group {group_id} not found")
    
    #TODO: Check that the current user is in owner list
    await Groups.filter(id=group_id).update(**group.dict(exclude_unset=True))
    return await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))

    #TODO: Return exception if not in owner list

async def delete_group(group_id, current_user) -> Status:
    try:
        db_group = await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Group {group_id} not found")

    #TODO: Check that the current user is in owner list
    deleted_count = await Groups.filter(id=group_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Group {group_id} not found")
    return Status(message=f"Deleted group {group_id}")

    #TODO: Return exception if not in owner list

