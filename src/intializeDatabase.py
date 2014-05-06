"""
This file will be used to define and initialize
the database that will store all of the historical price data for stocks,
should be expanded in the future to include more than just stocks




"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()





engine = create_engine('sqlite:///testing_database.db')

Base.metadata.create_all(engine)



