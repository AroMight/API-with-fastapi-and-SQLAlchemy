from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from database.base_model import BaseModel


class TeamModel(BaseModel):
    """team model"""
    __tablename__ = 'teams'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    game: Mapped[str] = mapped_column(String(50))
    # relationship with players
    players = relationship('PlayerModel', back_populates='team')

    def __repr__(self):
        return f'<Team {self.name}>'
