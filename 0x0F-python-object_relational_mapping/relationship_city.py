#!/usr/bin/python3
"""a script that contains city class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """the class with the name,id and state_id attr of individual city"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
