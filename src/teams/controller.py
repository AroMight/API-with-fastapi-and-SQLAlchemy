from uuid import uuid4
from datetime import datetime
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import APIRouter, HTTPException, status, Depends, Body
from pydantic import UUID4
from database.session import get_session
from teams.schema import TeamIn, TeamOut, TeamUpdate
from teams.model import TeamModel

router = APIRouter()


@router.post(
    "/teams/",
    status_code=status.HTTP_201_CREATED,
    response_description="Team created successfully",
    response_model=TeamOut,
)
async def create_user(
        team: Annotated[TeamIn, Body()],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    """Create a new team"""
    new_team = TeamModel(
        created_at=datetime.now(),
        uuid=uuid4(),
        **team.model_dump()
    )
    session.add(new_team)
    await session.commit()
    return new_team


@router.get(
    "/teams/all/",
    status_code=status.HTTP_200_OK,
    response_description="All teams",
    response_model=list[TeamOut],
)
async def get_all_teams(
        sessions: Annotated[AsyncSession, Depends(get_session)]
):
    """Get all teams"""
    teams = (await sessions.execute(select(TeamModel))).scalars().all()
    return teams


@router.get(
    "/teams/name/{team_name}/",
    status_code=status.HTTP_200_OK,
    response_description="Searched team",
    response_model=TeamOut,
)
async def get_team_by_name(
    session: Annotated[AsyncSession, Depends(get_session)],
    team_name: str,
):
    """Get team by name"""
    team = (await session.execute(select(TeamModel).filter_by(name=team_name))).scalars().first()

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team with name '{team_name}' found."
        )

    return team


@router.get(
    "/teams/id/{team_id}/",
    status_code=status.HTTP_200_OK,
    response_description="Searched team",
    response_model=TeamOut,
)
async def get_team_by_id(
    session: Annotated[AsyncSession, Depends(get_session)],
    team_id: UUID4
):
    """Get team by id"""
    team = (await session.execute(select(TeamModel).filter_by(uuid=team_id))).scalars().first()

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team with id '{team_id}' found."
        )

    return team


@router.patch(
    "/teams/id/{team_id}/",
    status_code=status.HTTP_200_OK,
    response_description="Team updated successfully",
    response_model=TeamOut,
)
async def update_team(
    session: Annotated[AsyncSession, Depends(get_session)],
    team_id: UUID4,
    updated_data: TeamUpdate,
):
    team = (await session.execute(select(TeamModel).filter_by(uuid=team_id))).scalars().first()
    team_update = updated_data.model_dump(exclude_unset=True)

    for key, value in team_update.items():
        setattr(team, key, value)

    await session.commit()
    await session.refresh(team)

    return team
