from pydantic import BaseModel, Field
from typing import Annotated

class User(BaseModel):
    id: Annotated[int, Field(description="The user's unique identifier")]
    name: Annotated[str, Field(description="The user's name")]
    email: Annotated[str, Field(description="The user's email address")]
    age: Annotated[int, Field(description="The user's age")]

    class Config:
        orm_mode = True
        extra = "forbid"