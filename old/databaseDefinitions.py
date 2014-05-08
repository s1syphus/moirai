"""


The entry needs to be changed to use .csv
That seems to be the only way to get large amounts of historical prices


When switching to live trading will need to be able to get live updates,
but for the purposes of 


Robert Micatka
May 6th, 2014
"""

import yahooFinance

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.types import Date, Numeric

"""
Database definition stuff

"""

Base = declarative_base()

class database:
    def __init__(self,location):
    #    self.Base = declarative_base()
        self.engine = create_engine(location)
        Base.metadata.create_all(self.engine)
          
    #This should probably be restructured for efficiency, just trying to
    #make things work currently
    def add_company(self,symbol):
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_company = Company(symbol=symbol)
        session.add(new_company)
        session.commit()

    def add_daily_prices(self,symbol,start_date,end_date):
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        hist_price = yahooFinance.get_historical_prices(symbol,start_date,end_date)
        for date in hist_price:     
            new_price = DailyStockPrice(date = date,
                                    volume = int(hist_price[date]['Volume']),
                                    adjClose = float(hist_price[date]['Adj Close']),
                                    high = float(hist_price[date]['High']),
                                    low = float(hist_price[date]['Low']),
                                    close = float(hist_price[date]['Close']),
                                    open = float(hist_price[date]['Open']),
                                    company_symbol = symbol)
            session.add(new_price)
            
        session.commit()


    
class Company(Base):
    __tablename__ = 'company'
    symbol = Column(String(250), primary_key=True)
    #other attributes?    
        
class DailyStockPrice(Base):
    # eventually might have to restructure this to optimize order, currently
    # the date is a string, cannot easily be indexed, sqlite3 is causing
    # problems though and doesn't play nicely with the datetime format
    __tablename__ = 'dailystockprice'
    date = Column(String(250), primary_key = True)
    volume = Column(Integer)
    adjClose = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    open = Column(Numeric)
    company_symbol = Column(Integer, ForeignKey('company.symbol'))
    company = relationship(Company)    
    
"""       
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

"""












