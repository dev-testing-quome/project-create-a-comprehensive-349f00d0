```python
import logging
import os
from typing import Generator

from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DATABASE_URL: str = os.getenv('DATABASE_URL', 'sqlite:///./app.db')

# Create database engine
try:
    engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
    logging.info(f"Connected to database: {DATABASE_URL}")
except exc.SQLAlchemyError as e:
    logging.critical(f"Failed to connect to database: {e}")
    raise

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator[sessionmaker, None, None]:
    """Provides a database session using a context manager.

    Yields:
        sessionmaker: A SQLAlchemy sessionmaker object.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
```