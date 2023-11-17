from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host_name: str
    port: int
    user_name: str
    password: str

    model_config = SettingsConfigDict( env_file='~/Restourant2/.env', extra='ignore')

settings = Settings()