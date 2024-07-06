from database.base_schema import BaseSchema
from typing import Annotated
from pydantic import Field, UUID4


class PlayerOut(BaseSchema):
    first_name: Annotated[str | None, Field(
        max_length=50, examples="John")] = None
    last_name: Annotated[str | None, Field(
        max_length=50, examples="Doe")] = None
    username: Annotated[str, Field(max_length=10)]
    email: Annotated[str, Field(max_length=50)]
    id_team: Annotated[int | None, Field()] = None


class PlayerIn(PlayerOut):
    password: Annotated[str, Field(min_length=8, max_length=16)]
