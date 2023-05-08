from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, DateTime, text

import os

# Get environment variables
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "mydatabase")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "myuser")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "mypassword")

# Create engine and session
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
print(DATABASE_URL)


class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, server_default=text("(now() at time zone 'utc')"))
    modified_at = Column(DateTime, nullable=False, server_default=text("(now() at time zone 'utc')"))
    created_by = Column(Integer, nullable=True)


# Create a dependency function to provide a database session to each endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()