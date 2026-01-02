# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Persistent SQLite database
engine = create_engine('sqlite:///cookies.db', echo=True)  # echo=True logs SQL

# 2. Session factory
SessionLocal = sessionmaker(bind=engine)

# 3. Base class for ORM models
Base = declarative_base()

# 4. Helper function to create all tables
def create_tables():
    Base.metadata.create_all(engine)
    
