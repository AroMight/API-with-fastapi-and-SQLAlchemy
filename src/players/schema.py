from database.base_schema import BaseSchema
from typing import Annotated
from pydantic import UUID4, Field
from teams.schema import TeamIn


class Player(BaseSchema):
    first_name: Annotated[str | None, Field(
        max_length=50, example="John", description="Player's first name. Can be null.")] = None
    last_name: Annotated[str | None, Field(
        max_length=50, example="Doe", description="Player's last name. Can be null.")] = None
    username: Annotated[str, Field(
        max_length=10, example="johndoe", description="Player's username")]
    email: Annotated[str, Field(
        max_length=50, example="jhon@doe.com.br", description="Player's email")]

class PlayerIn(Player):
    password: Annotated[str, Field(
        min_length=8, max_length=16, description="Player's password")]
    team: Annotated[TeamIn | None, Field(description="Player's team")] = None

class PlayerOut(Player):
    uuid: Annotated[UUID4, Field(description="Player's ID")]



class PlayerUpdate(BaseSchema):
    pass
