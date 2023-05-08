from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "mydatabase")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "myuser")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "mypassword")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
