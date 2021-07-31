import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
# from dotenv import load_dotenv
# load_dotenv()
# postgresql://scott:tiger@localhost/test
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_USER = os.environ.get('POSTGRES_USER')

engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}', echo = True)
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
