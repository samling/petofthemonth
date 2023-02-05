from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import PetImages
from src.schemas.petimages import PetImageOutSchema
from src.schemas.token import Status

async def get_pet_images():
    return await PetImageOutSchema.from_queryset(PetImages.all())

async def get_pet_image(pet_image_id) -> PetImageOutSchema:
    return await PetImageOutSchema.from_queryset_single(PetImages.get(id=pet_image_id))

async def create_pet_image(petimage, current_user) -> PetImageOutSchema:
    pet_image_dict = petimage.dict(exclude_unset=True)
    pet_image_obj = await PetImages.create(**pet_image_dict)
    return await PetImageOutSchema.from_tortoise_orm(pet_image_obj)

async def update_pet_image(pet_image_id, petimage, current_user) -> PetImageOutSchema:
    try:
        db_petimage = await PetImageOutSchema.from_queryset_single(PetImages.get(id=pet_image_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pet image {pet_image_id} not found")
    
    #TODO: Check that the current user is in owner list
    await PetImages.filter(id=pet_image_id).update(**petimage.dict(exclude_unset=True))
    return await PetImageOutSchema.from_queryset_single(PetImages.get(id=pet_image_id))

    #TODO: Return exception if not in owner list

async def delete_pet_image(pet_image_id, current_user) -> Status:
    try:
        db_petimage = await PetImageOutSchema.from_queryset_single(PetImages.get(id=pet_image_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Pet image {pet_image_id} not found")

    #TODO: Check that the current user is in owner list
    deleted_count = await PetImages.filter(id=pet_image_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Pet image {pet_image_id} not found")
    return Status(message=f"Deleted pet image {pet_image_id}")

    #TODO: Return exception if not in owner list
