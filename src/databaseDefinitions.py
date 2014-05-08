"""
This file will be used to define and initialize
the database that will store all of the historical price data for stocks,
should be expanded in the future to include more than just stocks

Robert Micatka
May 7th, 2014

"""

import time
import sqlite3
import csv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = None #change this later

class DailyStockPrice(Base):
    __tablename__ = 'dailystockprice'
    #date is an integer of YYYYMMDD format
    date = Column(Integer, primary_key = True)
    volume = Column(Integer)
    adjClose = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    open = Column(Numeric) 
    symbol = Column(String(10))
    exchange = Column(String(10))
    
def init_dailyStockPrice(dbname):
    global engine
    engine = create_engine(dbname, echo=False)
    DBSession.remove()
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def load_csv(csv_file):
    with open(csv_file) as f:
        cf = csv.DictReader(f,delimiter=',')
        for row in cf:
            
    




