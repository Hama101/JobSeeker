"""
    -This mainly used to create a database connection session engine.
"""
from sqlalchemy import create_engine
from config import settings


engine = create_engine(
    settings.database_url, echo=settings.ECHO_SQL,
)

