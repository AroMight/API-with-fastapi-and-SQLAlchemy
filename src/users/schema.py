from pydantic import Field
from typing import Annotated
from schemas.base import BaseSchema


class User(BaseSchema):
    id: Annotated[int, Field(description="The user's ID", example=1, ge=1)] = 1
    name: Annotated[str, Field(
        description="The user's name", example="John Doe", max_length=50)]
    email: Annotated[str, Field(
        description="The user's email address", example="lol@lol.com")]
    age: Annotated[int, Field(description="The user's age", example=25, ge=18)]
    password: Annotated[str, Field(
        description="The user's password", example="password", min_length=8, max_length=50)]


class OutMixin(BaseSchema):
    id: Annotated[int, Field(description="The user's ID", example=1, ge=1)] = 1


class UserOut(OutMixin):
    name: Annotated[str, Field(
        description="The user's name", example="John Doe", max_length=50)]
    email: Annotated[str, Field(
        description="The user's email address", example="lol@lol.com")]
    age: Annotated[int, Field(description="The user's age", example=25, ge=18)]


class UserIn(UserOut):
    password: Annotated[str, Field(
        description="The user's password", example="password", min_length=8, max_length=50)]
