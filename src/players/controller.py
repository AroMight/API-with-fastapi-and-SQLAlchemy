from typing import Annotated
from datetime import datetime
from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi import status
from src.teams.model import TeamModel
from src.players.schema import PlayerIn, PlayerOut
from src.players.model import PlayerModel
from src.database.session import AsyncSession, get_session


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
    """Create a new player in the database."""
    team_name = player.team.name
    player_team = (
        await session.execute(select(TeamModel).filter_by(name=team_name))
    ).scalars().first()

    if not player_team:
        raise HTTPException(status_code=404, detail="Team not found")

    player_data = player.model_dump(exclude='team')

    try:
        new_player = PlayerModel(
            id_team=player_team.id, created_at=datetime.now(), uuid=uuid4(), **player_data)
        session.add(new_player)
        await session.commit()

    # future improvement: give more details about the error
    except IntegrityError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="The username or email is already in use") from exc

    return new_player


@router.get(
    "/players/all",
    response_model=list[PlayerOut],
    status_code=status.HTTP_200_OK,
)
async def get_all_players(
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Get all players."""
    players = (await session.execute(select(PlayerModel))).scalars().all()
    return players


@router.get(
    "/players/{player_id}",
    response_model=PlayerOut,
    status_code=status.HTTP_200_OK,
)
async def get_player(
    session: Annotated[AsyncSession, Depends(get_session)],
    player_id: Annotated[UUID4, Path(title="The ID of the player")],
):
    """Get a player by ID."""
    player = (
        await session.execute(select(PlayerModel).filter_by(uuid=player_id))
    ).scalars().first()

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player


@router.get(
    "/players/{player_username}/",
    response_model=PlayerOut,
    status_code=status.HTTP_200_OK,
)
async def get_player_by_username(
    session: Annotated[AsyncSession, Depends(get_session)],
    player_username: Annotated[str, Path(title="The username of the player")],
):
    """Get a player by username."""
    player = (
        await session.execute(select(PlayerModel).filter_by(username=player_username))
    ).scalars().first()

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player

@router.delete(
    "/players/{player_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_player(
    session: Annotated[AsyncSession, Depends(get_session)],
    player_id: Annotated[UUID4, Path(title="The ID of the player")],
):
    """Delete a player by ID."""
    player = (
        await session.execute(select(PlayerModel).filter_by(uuid=player_id))
    ).scalars().first()

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    session.delete(player)
    await session.commit()