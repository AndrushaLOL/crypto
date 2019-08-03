import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db.config import DATABASE_URI


engine = sqlalchemy.create_engine(DATABASE_URI)
conn = engine.connect()
metadata = sqlalchemy.MetaData()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from db import models

Base.metadata.create_all(engine)