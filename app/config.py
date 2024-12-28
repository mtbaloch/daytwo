from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DATABASE_URL: str
    TITLE: str = Field(default="Student API", description="Title of the API")
    DESCRIPTION: str = Field(default="Student API to register students", description="Description of the API")
    VERSION: str = Field(default="0.0.1", description="Version of the API")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
