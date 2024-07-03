from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from .base_settings import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{
        settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)
engine = create_async_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, class_=AsyncSession,
                       expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with Session() as session:
        yield session
