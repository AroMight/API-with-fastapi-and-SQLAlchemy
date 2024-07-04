from datetime import datetime
from typing import Annotated
from pydantic import Field, UUID4
from database.base_schema import BaseSchema


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
    uuid: Annotated[UUID4, Field(description='Team ID')]
    created_at: Annotated[datetime, Field(description='Team creation date')]
