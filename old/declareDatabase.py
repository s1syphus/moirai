"""
This file will be used to define and initialize
the database that will store all of the historical price data for stocks,
should be expanded in the future to include more than just stocks

Robert Micatka
May 6th, 2014

"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.types import Date, Numeric

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key = True)
    symbol = Column(String(250), nullable=False)
    #other attributes?
    
class DailyStockPrice(Base):
    __tablename__ = 'dailystockprice'
    date = Column(Date, primary_key = True)
    volume = Column(Integer)
    adjClose = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    open = Column(Numeric) 
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship(Company)
    
    
engine = create_engine('sqlite:///testing_database.db')

Base.metadata.create_all(engine)



