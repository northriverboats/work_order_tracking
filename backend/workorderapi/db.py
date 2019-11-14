import os
from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

load_dotenv()
engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])

Session = scoped_session(sessionmaker(bind=engine))
