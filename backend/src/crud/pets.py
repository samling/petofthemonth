from fastapi import HTTPException
from tortoise import Tortoise
from tortoise.exceptions import DoesNotExist

from src.database.models import Pets, Points, Groups, Users
from src.schemas.pets import PetOutSchema
from src.schemas.points import PointOutSchema
from src.schemas.users import UserOutSchema
from src.schemas.token import Status

async def get_pets():
    print(PetOutSchema.schema_json(indent=4))
    return await PetOutSchema.from_queryset(Pets.all())

async def get_pet(pet_id) -> PetOutSchema:
    return await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))

async def create_pet(pet, current_user) -> PetOutSchema:
    user_obj = await Users.filter(id=current_user.id).first()

    pet_dict = pet.dict(exclude_unset=True)
    pet_obj = await Pets.create(**pet_dict)
    await pet_obj.users.add(user_obj)
    return await PetOutSchema.from_tortoise_orm(pet_obj)

async def create_pet_point(pet_id, point, current_user) -> PointOutSchema:
    try:
        db_pet = await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pet {pet_id} not found")

    point_dict = point.dict(exclude_unset=True)
    point_obj = await Points.create(**point_dict, pet_id=pet_id)
    return await PointOutSchema.from_tortoise_orm(point_obj)

async def update_pet_users(request, pet_id, pet, user_id, current_user) -> PetOutSchema:
    try:
        db_pet = await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pet {pet_id} or user {user_id} not found")
    
    pet_obj = await Pets.filter(id=pet_id).first()
    user_obj = await Users.filter(id=current_user.id).first()
    if user_obj in pet_obj.users:
        if request.method == 'PATCH':
            await pet_obj.users.add(user_obj)
        elif request.method == 'DELETE':
            # Check to make sure we're not removing the last user
            if len(pet_obj.users) > 1: # TODO: Check to make sure we're not removing ourselves(?)
                await pet_obj.users.remove(user_obj)
            else:
                raise HTTPException(status_code=403, detail=f"Pet cannot have no owners")
        return await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))

    raise HTTPException(status_code=403, detail=f"Not authorized")

async def update_pet(pet_id, pet, current_user) -> PetOutSchema:
    try:
        db_pet = await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pet {pet_id} not found")
    
    #TODO: Check that the current user is in owner list
    await Pets.filter(id=pet_id).update(**pet.dict(exclude_unset=True))
    return await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))

    #TODO: Return exception if not in owner list

async def delete_pet(pet_id, current_user) -> Status:
    try:
        db_pet = await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pet {pet_id} not found")

    #TODO: Check that the current user is in owner list
    deleted_count = await Pets.filter(id=pet_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Pet {pet_id} not found")
    return Status(message=f"Deleted pet {pet_id}")

    #TODO: Return exception if not in owner list