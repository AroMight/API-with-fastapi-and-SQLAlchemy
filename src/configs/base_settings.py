from pydantic_settings import BaseSettings, SettingsConfigDict

# import Pydantic base settings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    
    db_url: str


settings = Settings()
