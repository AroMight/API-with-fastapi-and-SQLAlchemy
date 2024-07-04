from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from src.database.base_model import BaseModel


class PlayerModel(BaseModel):
    """Player model"""
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(
        String(10), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(16), nullable=False)
    id_team: Mapped[int] = mapped_column(
        Integer, ForeignKey('teams.id'), nullable=True)
    # relationship with team
    team = relationship('Team', back_populates='players')

    def __repr__(self):
        return f'<Player {self.username}>'
