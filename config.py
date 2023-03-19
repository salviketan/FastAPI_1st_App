import os
from dotenv import load_dotenv

load_dotenv(dotenv_path= ".env")

class Settings:
    TITLE = "First Fastapi app config"
    VERSION = "0.0.1"
    DECRIPTION = """
    ## This is 1st Fastapi app
    config
    """
    NAME = "Fastapi"
    EMAIL = "fastapi@email.com"
    PG_USER = os.getenv("DB_USER")
    PG_PASSWD = os.getenv("DB_PASSWD")
    PG_HOST = os.getenv("DB_HOST", "localhost")
    PG_PORT = os.getenv("DB_PORT", 5432)
    PG_DB = os.getenv("DB_NAME")
    DB_URL = f"postgresql://{PG_USER}:{PG_PASSWD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

settings = Settings()