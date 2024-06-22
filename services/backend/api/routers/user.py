from fastapi import APIRouter, HTTPException
from typing import List

from api.schemas.user import UserCreate, UserResponse
from api.services.user import (
    get_user, create_user_service, get_users
)

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    """
    Create a new user.

    Args:
        user (UserCreate): The user data for the new user.

    Returns:
        UserResponse: The created user data.

    Raises:
        HTTPException: If an error occurs during user creation.
    """
    try:
        db_user = await create_user_service(user=user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[UserResponse])
async def read_users(skip: int = 0, limit: int = 10):
    """
    Retrieve a list of users with pagination.

    Args:
        skip (int, optional): The number of users to skip. Defaults to 0.
        limit (int, optional): The maximum number of users to return. Defaults to 10.

    Returns:
        List[UserResponse]: A list of user data.
    """
    users = await get_users(skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    """
    Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserResponse: The user data if found.

    Raises:
        HTTPException: If the user is not found.
    """
    db_user = await get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user