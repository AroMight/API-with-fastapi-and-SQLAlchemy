from fastapi import APIRouter, Path
from users.schema import UserIn, UserOut, User
from typing import Annotated
from configs.tags import Tags

router = APIRouter()


@router.post(
    "/users/{id}",
    response_model=UserOut,
    tags=[Tags.USERS],
)
async def create_user(user: UserIn, id: Annotated[int, Path(ge=1)]):
    new_user = User(**user.model_dump(), id=id)
    return new_user
