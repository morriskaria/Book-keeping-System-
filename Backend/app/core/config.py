from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application Settings.
    This class loads variables from the environment (e.g., .env file)
    or uses the default values provided here.
    """
    PROJECT_NAME: str = "Hospital Bookkeeping System"
    # The default URL is for a local SQLite database named 'bookkeeping.db'
    DATABASE_URL: str = "sqlite:///./bookkeeping.db"

    class Config:
        env_file = ".env"

# Create a single instance of settings to be used throughout the app
settings = Settings()
