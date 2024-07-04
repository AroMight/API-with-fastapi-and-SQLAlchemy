from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from configs.base_settings import settings

DATABASE_URL = (settings.db_url)
engine = create_async_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, class_=AsyncSession,
                       expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with Session() as session:
        yield session
