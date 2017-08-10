import psycopg2
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    phone = Column(String(11), nullable = False)
    email = Column(String(80), nullable = False)

engine = create_engine('sqlite://signedup.db')

Base.metadata.create_all(engine)