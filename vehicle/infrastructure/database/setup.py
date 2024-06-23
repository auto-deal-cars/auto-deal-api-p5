"""
This module contains the database setup for the vehicle application.
"""
import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

def is_running_with_alembic():
    """
    Check if the current process is running with Alembic.
    """
    return 'alembic' in sys.modules

def setup_database():
    """
    Setup the database connection and session.
    """
    if is_running_with_alembic():
        load_dotenv()

    database_url = os.getenv("DATABASE_URL") or "sqlite:///:memory:"
    engine = create_engine(database_url)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    base = declarative_base()

    return engine, session_local, base

engine, SessionLocal, Base = setup_database()

def get_db():
    """
    This function returns a session to the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
