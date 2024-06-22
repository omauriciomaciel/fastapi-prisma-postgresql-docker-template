from typing import Optional
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    """
    Base model for user data.

    Attributes:
        username (str): The username of the user.
    """
    username: str

class UserCreate(UserBase):
    """
    Model for creating a new user, extending from UserBase.

    Inherits:
        UserBase (BaseModel): Base model for user data.
    """
    pass

class UserResponse(UserBase):
    """
    Model for user response data, extending from UserBase.

    Attributes:
        id (int): The unique identifier of the user.

    Inherits:
        UserBase (BaseModel): Base model for user data.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
