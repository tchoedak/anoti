import sqlite3
import config
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker


_db = f"{config.app}.db"
engine = create_engine(f'sqlite:///{_db}')
_sessionmaker = sessionmaker(bind=engine)
session = _sessionmaker()

def create_db():
    conn = sqlite3.connect(f"{config.app}.db")
    print(sqlite3.version)

