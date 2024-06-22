from typing import List, Optional

from api.schemas import user
from api.connection import prisma_connection

async def get_user(user_id: int) -> Optional[user.UserResponse]:
    """
    Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        Optional[user.UserResponse]: The user data if found, otherwise None.
    """
    return await prisma_connection.db.user.find_unique(where={"id": user_id})

async def create_user_service(user: user.UserCreate) -> user.UserResponse:
    """
    Create a new user in the database.

    Args:
        user (user.UserCreate): The user data for the new user.

    Returns:
        user.UserResponse: The created user data.
    """
    async with prisma_connection.db.tx() as transaction:
        return await transaction.user.create(data={"username": user.username})

async def get_users(skip: int = 0, limit: int = 10) -> List[user.UserResponse]:
    """
    Retrieve a list of users with pagination.

    Args:
        skip (int, optional): The number of users to skip. Defaults to 0.
        limit (int, optional): The maximum number of users to return. Defaults to 10.

    Returns:
        List[user.UserResponse]: A list of user data.
    """
    return await prisma_connection.db.user.find_many(skip=skip, take=limit)