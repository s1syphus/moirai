"""
This will contain all of the class definitions for 
the backtesting module


Robert Micatka
May 17th, 2014
"""

class stock:
    def __init__(self, symbol, buyDate, buyPrice, numberShares):
        #not sure if I need this or not
        self.symbol = symbol;
        self.buyPrice = buyPrice;
        self.numberShares = numberShares;
        
    def buy(self, symbol, buyDate, buyPrice, numberShares):
        self.symbol = symbol;
        self.buyDate = buyDate;
        self.buyPrice = buyPrice;
        self.numberShares = numberShares;
    
    def getSymbol(self):
        return self.symbol
    
    def getNumberShares(self):
        return int(self.numberShares)
    
    def getCurrentPrice(self, date):
        #this needs to be fixed to read in data about the day
        return self.buyPrice
    
class user:
    def __init__(self,userName,startingDate,startingCash,  commissionFee):
        self.userName = userName;
        self.currentCash = startingCash;
        self.startingDate = startingDate;
        self.commissionFee = commissionFee;
        self.stocks = []
        
    def buy(self,symbol, buyDate, buyPrice, numberShares):
        tempStock = stock(symbol, buyDate, buyPrice, numberShares);
        self.stocks.append(tempStock)
        self.currentCash = self.currentCash - float(numberShares) * float(buyPrice)* (1 + float(self.commissionFee));
        
    def printData(self,date):
        self.date = '2000-01-01'
        print("Username = %s" % self.userName)
        print("Cash = %.2f" % self.currentCash)
        self.netWorth =self.currentCash
        print("Stocks:")
        for i in self.stocks:
            stockValue = i.getNumberShares() * i.getCurrentPrice(self.date)
            print("%s %i %0.2f %0.2f" % (i.getSymbol(), i.getNumberShares(), i.getCurrentPrice(self.date), stockValue))
            self.netWorth += stockValue
        print("Net Worth = %.2f" % self.netWorth)
        
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
"""
