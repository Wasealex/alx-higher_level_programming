#!/usr/bin/python3
"""module that contains the class definition of a State
   and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """inherits from Base
       links to the MySQL table states
       attributes
                 id that represents a column of an auto-generated,
                                                   unique integer,
                                                   is a primary key
                 name that represents a column of a string with
                                                   maximum 128 characters and
                                                   can’t be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
