from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Claims RAG Assistant"
    top_k: int = 5
    data_dir: Path = Path("data")
    model_config = SettingsConfigDict(env_file=".env", env_prefix="CLAIMS_RAG_")


settings = Settings()
