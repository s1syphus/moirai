"""
This file will be used to define and initialize
the database that will store all of the historical price data for stocks,
should be expanded in the future to include more than just stocks

Robert Micatka
May 7th, 2014

"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, create_engine,Float
from sqlalchemy.orm import scoped_session, sessionmaker

import csv


engine = create_engine('sqlite:///../data/testDB2.db')
Base = declarative_base()

"""
class DailyStockPrice(Base):
    __tablename__ = 'dailyStockPrice'
    exchange = Column(String(10), primary_key=True)
    stock_symbol = Column(String(10), primary_key=True)
    #date is an string of YYYY-MM-DD format
    date = Column(String(10), primary_key=True)
    stock_price_open = Column(Numeric)
    stock_price_high = Column(Numeric)
    stock_price_low = Column(Numeric)
    stock_price_close = Column(Numeric)
    stock_volume = Column(Integer)
    stock_price_adj_close = Column(Numeric)
"""

class DailyStockPrice(Base):
    __tablename__ = 'dailyStockPrice'
    exchange = Column(String(10), primary_key=True)
    symbol = Column(String(10), primary_key=True)
    #date_ is an string of YYYY-MM-DD format
    date_ = Column(String(10), primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    adj_close = Column(Float)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
counter = 0

"""
with open('old.csv') as csvfile:
    file_ = csv.reader(csvfile, delimiter=',')
    for row in file_:
        counter = counter + 1
        test_stock = DailyStockPrice(exchange=row[0], symbol=row[1],date_=row[2],
                                     open=float(row[3]),high=float(row[4]),low=float(row[5]),close=float(row[6]),
                                     volume=int(row[7]),adj_close=float(row[8]))
        session.add(test_stock)
        if (counter % 50000) == 0:
            session.commit()
            print("committed, counter = %i" % counter)

session.commit()
"""

for instance in session.query(DailyStockPrice).filter(DailyStockPrice.date_=='2005-01-05'):
    print(instance.symbol)
