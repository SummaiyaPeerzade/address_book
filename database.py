from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# connecting to a SQLite database (opening a file(./address_book.db) with the SQLite database).

SQLALCHEMY_DATABASE_URL = "sqlite:///./address_book.db"

#creating a SQLAlchemy engine.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #connect_args used only for SQLite
)
#creating session for database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() #returns a class
