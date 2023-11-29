from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host_name: str
    port: int
    user_name: str
    password: str
    database_url: str
    db_name: str
    test_db_name: str
    redis_host: str
    redis_port: int
    redis_database: int
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict( env_file='~/Restourant2/.env', extra='ignore')

settings = Settings()