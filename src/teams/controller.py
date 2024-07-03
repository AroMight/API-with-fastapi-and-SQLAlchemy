from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends, Body
from configs.session import get_session
from teams.schema import TeamIn, TeamOut
from typing import Annotated
from teams.model import TeamModel


router = APIRouter()


@router.post(
    "/teams/",
    status_code=status.HTTP_201_CREATED,
    response_description="Create a new user",
    response_model=TeamOut,
)
async def create_user(
        team: Annotated[TeamIn, Body()],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    new_team = TeamModel(
        created_at=datetime.now(timezone.utc),
        uuid=uuid4(),
        **team.model_dump()
    )
    session.add(new_team)
    await session.commit()
    return new_team
