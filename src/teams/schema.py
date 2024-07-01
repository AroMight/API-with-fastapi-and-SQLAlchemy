from datetime import datetime
from pydantic import Annotated, Field, UUID4
from schemas.base import BaseSchema


class Team(BaseSchema):
    """Team schema"""
    name: Annotated[str, Field(
        max_length=50, description="Team's name", example='Team A')]
    game: Annotated[str, Field(
        max_length=50, description="The game which the team plays", example='God of War')]


class TeamIn(Team):
    """TeamIn schema"""
    pass


class TeamOut(Team):
    """TeamOut schema"""
    id: Annotated[UUID4, Field(description='Team ID')]
    created_at: Annotated[datetime, Field(description='Team creation date')]
