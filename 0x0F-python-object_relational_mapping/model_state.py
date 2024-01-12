#!/usr/bin/python3
"""a script that contains state class and Base
an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """the class with the name and id attr of individualll state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
