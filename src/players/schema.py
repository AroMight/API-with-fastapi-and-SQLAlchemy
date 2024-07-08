from typing import Annotated
from pydantic import UUID4, Field, EmailStr
from src.database.base_schema import BaseSchema
from src.teams.schema import TeamIn
from pydantic import field_validator
import re


class Player(BaseSchema):
    first_name: Annotated[str | None, Field(
        max_length=50, example="John", description="Player's first name. Can be null.")] = None
    last_name: Annotated[str | None, Field(
        max_length=50, example="Doe", description="Player's last name. Can be null.")] = None
    username: Annotated[str, Field(
        max_length=10, example="johndoe", description="Player's username")]
    email: Annotated[EmailStr, Field(
        max_length=50, example="jhon@doe.com.br", description="Player's email")]


class PlayerIn(Player):
    password: Annotated[str, Field(
        min_length=8, max_length=16, description="Player's password", example="Exemple@123")]
    team: Annotated[TeamIn | None, Field(description="Player's team")] = None

    @field_validator('password')
    def validate_password(cls, value: str) -> str:
        if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=]).{8,}$", value):
            raise ValueError(
                "Password must have at least 8 characters, 1 uppercase, 1 lowercase, 1 number and 1 special character.")
        return value


class PlayerOut(Player):
    uuid: Annotated[UUID4, Field(description="Player's ID")]


class PlayerUpdate(BaseSchema):
    pass
