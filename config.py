"""
This file contains the configuration for the application.
mainly we will have the database configuration here.
and the secret key for the application.
and the settings for the application.
"""

import os
from typing import (
    Optional,
)

from pydantic import (
    BaseSettings,
)

# load the environment variables from the .env file.
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    
    # --- Application settings ---
    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "Job Seeker")
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "secret")
    DEBUG: Optional[bool] = bool(int(os.environ.get("DEBUG", 0)))

    # --- API settings ---
    UNSPLASH_CLIENT_ID: str = os.environ.get("UNSPLASH_CLIENT_ID", None)
    UNSPLASH_URL : str = os.environ.get("UNSPLASH_URL", "https://api.unsplash.com/search/photos/?")
    JOB_URL : str = os.environ.get("JOB_URL", "https://careers.google.com/api/v3/search/?")


    # --- Database Configuration ---
    # to keep everything simple we will use sqlite for the database.
    # but you can use any database you want.
    # just make sure to change the database url.
    DATABASE_URL : str = os.environ.get("DATABASE_URL", "sqlite:///database.db")

    # --- GUI settings ---
    WIDTH: int = int(os.environ.get("WIDTH", 1000))
    HEIGHT: int = int(os.environ.get("HEIGHT", 700))
    TITLE: str = os.environ.get("TITLE", "Job Searcher")
    ICON: str = os.environ.get("ICON", "icon.ico")

    # --- DIRS ---
    ASSETS_DIR : str = os.environ.get("ASSETS_DIR", "assets")
    IMAGES_DIR : str = os.environ.get("IMAGES_DIR", "images")
    LANGUAGES_LANGS_DIR : str = os.environ.get("LANGUAGES_LANGS_DIR", "languages_logs")
    
    # --- Files ---
    CURRENT_PATH : str = os.path.dirname(os.path.abspath(__file__))

    @property
    def database_url(self):
        return self.DATABASE_URL

    
    @property
    def job_url(self):
        return self.JOB_URL
