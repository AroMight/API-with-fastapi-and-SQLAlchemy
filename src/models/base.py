from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import UUID, DateTime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from datetime import datetime


class BaseModel(DeclarativeBase):
    uuid: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
