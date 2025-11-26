from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    PROVIDER_TOKEN: str
    DB_URL: str
    CURRENCY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()