"""
Calling this will populate the created database (in initializeDatabase.py)
using calls to yahooFinance.get_historical_prices()


Robert Micatka
May 6th, 2014
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from declareDatabase import Company, Base, DailyStockPrice

engine = create_engine('sqlite:///testing_database.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()




session.commit()





