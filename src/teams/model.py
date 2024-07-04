from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime
from src.database.base_model import BaseModel


class TeamModel(BaseModel):
    """team model"""
    __tablename__ = 'teams'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    game: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    # relationship with players
    players = relationship('Player', back_populates='team')

    def __repr__(self):
        return f'<Team {self.name}>'
