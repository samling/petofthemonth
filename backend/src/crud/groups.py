from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Groups, Pets, Users
from src.schemas.groups import GroupOutSchema
from src.schemas.pets import PetOutSchema
from src.schemas.users import UserOutSchema
from src.schemas.token import Status

async def get_groups():
    return await GroupOutSchema.from_queryset(Groups.all())

async def get_group(group_id) -> GroupOutSchema:
    return await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))

async def create_group(group, current_user) -> GroupOutSchema:
    user_obj = await Users.filter(id=current_user.id).first()

    group_dict = group.dict(exclude_unset=True)
    group_obj = await Groups.create(**group_dict)
    # TODO: Do we want to add the user by default? Probably
    await group_obj.users.add(user_obj)
    return await GroupOutSchema.from_tortoise_orm(group_obj)

async def update_group_users(request, group_id, user_id, current_user) -> GroupOutSchema:
    try:
        db_group = await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Group {group_id} or user {user_id} not found")
    
    group_obj = await Groups.filter(id=group_id).first()
    user_obj = await Users.filter(id=current_user.id).first()
    if user_obj in group_obj.users:
        if request.method == 'PATCH':
            await group_obj.users.add(user_obj)
        elif request.method == 'DELETE':
            # Check to make sure we're not removing the last user
            if len(group_obj.users) > 1: # TODO: Check to make sure we're not removing ourselves(?)
                await group_obj.users.remove(user_obj)
            else:
                raise HTTPException(status_code=403, detail=f"Group cannot have no members")
        return await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))

    raise HTTPException(status_code=403, detail=f"Not authorized")

async def update_group_pets(request, group_id, group, pet_id, current_user) -> GroupOutSchema:
    try:
        db_group = await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))
        db_pet = await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Group {group_id} or pet {pet_id} not found")
    
    #TODO: Check that the current user is in owner list
    group_obj = await Groups.filter(id=group_id).first()
    pet_obj = await Pets.filter(id=pet_id).first()
    if request.method == 'PATCH':
        await group_obj.pets.add(pet_obj)
    elif request.method == 'DELETE':
        # if pet_obj in group_obj.pets:
        #     print("exists")
        await group_obj.pets.remove(pet_obj)

    await Groups.filter(id=group_id).update(**group.dict(exclude_unset=True))
    return await GroupOutSchema.from_queryset_single(Groups.get(id=group_id))

    #TODO: Return exception if not in owner list

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

