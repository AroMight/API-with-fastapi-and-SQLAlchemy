from pydantic_settings import BaseSettings, SettingsConfigDict

# import Pydantic base settings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: int

    @property
    def db_url(self) -> str:
        """Returns the database URL"""
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.db_host}:{self.db_port}/{self.postgres_db}"


settings = Settings()
