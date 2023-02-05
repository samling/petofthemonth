from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.petimages as crud
from src.auth.jwthandler import get_current_user
from src.schemas.petimages import PetImageInSchema, PetImageOutSchema, UpdatePetImage
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
    "/petimages",
    response_model=List[PetImageOutSchema],
    # response_model_exclude=exclude_user_password_pattern,
    dependencies=[Depends(get_current_user)]
)
async def get_points():
    return await crud.get_points()

@router.get(
    "/petimage/{pet_image_id}",
    response_model=PetImageOutSchema,
    # response_model_exclude=exclude_user_password_pattern,
    dependencies=[Depends(get_current_user)]
)
async def get_pet_image(
    pet_image_id: int
) -> PetImageOutSchema:
    try:
        return await crud.get_pet_image(pet_image_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Pet image does not exist"
        )

@router.post(
    "/petimages",
    response_model=PetImageOutSchema,
    # response_model_exclude=exclude_user_password_pattern,
    dependencies=[Depends(get_current_user)]
)
async def create_pet_image(
    petimage: PetImageInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> PetImageOutSchema:
    return await crud.create_pet_image(petimage, current_user)

@router.patch(
    "/petimage/{pet_image_id}",
    dependencies=[Depends(get_current_user)],
    response_model=PetImageOutSchema,
    # response_model_exclude=exclude_user_password_pattern,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_pet_image(
    pet_image_id: int,
    petimage: UpdatePetImage,
    current_user: UserOutSchema = Depends(get_current_user)
) -> PetImageOutSchema:
    return await crud.update_pet_image(pet_image_id, petimage, current_user)

@router.delete(
    "/petimage/{pet_image_id}",
    response_model=Status,
    # response_model_exclude=exclude_user_password_pattern,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)]
)
async def delete_pet_image(
    pet_image_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_pet_image(pet_image_id, current_user)