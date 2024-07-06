from database.base_schema import BaseSchema
from typing import Annotated
from pydantic import Field
from teams.schema import TeamIn


class PlayerOut(BaseSchema):
    first_name: Annotated[str | None, Field(
        max_length=50, example="John")] = None
    last_name: Annotated[str | None, Field(
        max_length=50, example="Doe")] = None
    username: Annotated[str, Field(max_length=10, example="johndoe")]
    email: Annotated[str, Field(max_length=50, example="jhon@doe.com.br")]


class PlayerIn(PlayerOut):
    password: Annotated[str, Field(min_length=8, max_length=16)]    
    team: Annotated[TeamIn | None, Field(description="Player's team")] = None