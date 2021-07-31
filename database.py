import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
# from dotenv import load_dotenv
# load_dotenv()

DB_NAME = os.environ.get('DB_URL')
engine = create_engine(DB_NAME, echo = True)
SessionLocal = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

def migrate():
    Base.metadata.create_all(engine)

def drop():
    Base.metadata.drop_all(engine)

def get_session():
    return SessionLocal()


if __name__ == '__main__':
    migrate()
