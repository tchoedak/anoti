import sqlite3
from . import config
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker


path = os.path.join(os.path.expanduser('~'))
_db = os.path.join(f"{path}", ".anoti.db")
url = f'sqlite:///{_db}'


def _engine():
    return create_engine(url)


def _session():
    _sessionmaker = sessionmaker(bind=_engine())
    return _sessionmaker()


def create_db():
    conn = sqlite3.connect(_db)
    print(sqlite3.version)


def _cursor():
    return sqlite3.connect(_db).cursor()


session = _session()
cursor = _cursor()


def save(*objects):
    for obj in objects:
        session.add(obj)
    session.commit()
