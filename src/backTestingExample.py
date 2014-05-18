"""
This is the main backtesting module
It will:
- Connect to the database
- Query for stocks
- integrate with trading strategies


Robert Micatka
May 8th, 2014
"""


from sqlalchemy import Column, Integer, String, Numeric, create_engine,Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DailyStockPrice(Base):
    __tablename__ = 'dailyStockPrice'
    exchange = Column(String(10), primary_key=True)
    symbol = Column(String(10), primary_key=True)
    #date_ is an string of YYYY-MM-DD format
    date = Column(String(10), primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    adj_close = Column(Float)


engine = create_engine('sqlite:///../data/amexDailyA.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#for instance in session.query(DailyStockPrice).filter(DailyStockPrice.symbol=="ABL").all():

for instance in session.query(DailyStockPrice).\
                filter(DailyStockPrice.symbol=="ABL").\
                filter(DailyStockPrice.date > "2000-01-01").\
                filter(DailyStockPrice.date < "2000-02-01"):
    print(instance.date)

