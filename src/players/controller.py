from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy import select
from players.schema import PlayerIn, PlayerOut
from players.model import PlayerModel
from typing import Annotated
from database.session import AsyncSession, get_session
from teams.model import TeamModel
from fastapi import status
from uuid import uuid4
from datetime import datetime


router = APIRouter()


@router.post(
    "/users/",
    response_model=PlayerOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_player(
    session: Annotated[AsyncSession, Depends(get_session)],
    player: PlayerIn,
):
    team_name = player.team.name
    player_team = (await session.execute(select(TeamModel).filter_by(name=team_name))).scalars().first()

    if not player_team:
        raise HTTPException(status_code=404, detail="Team not found")

    player_data = player.model_dump(exclude='team')

    new_player = PlayerModel(
        id_team=player_team.id, created_at=datetime.now(), uuid=uuid4(), **player_data)
    session.add(new_player)
    await session.commit()

    # add verification for email and username

    return new_player
