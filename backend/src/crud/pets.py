from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Pets
from src.schemas.pets import PetOutSchema
from src.schemas.token import Status

async def get_pets():
    return await PetOutSchema.from_queryset(Pets.all())

async def get_pet(pet_id) -> PetOutSchema:
    return await PetOutSchema.from_queryset_single(Pets.get(id=pet_id))

async def create_pet(pet, current_user) -> PetOutSchema:
    pet_dict = pet.dict(exclude_unset=True)
    pet_obj = await Pets.create(**pet_dict)
    return await PetOutSchema.from_tortoise_orm(pet_obj)

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