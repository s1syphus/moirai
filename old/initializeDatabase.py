"""
This file will be used to initialize companies

Robert Micatka
May 6th, 2014

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from declareDatabase import Company, Base


class database():
    database_location = 'sqlite:///testing_database.db'
    def connect_database(self,database_location):
        engine = create_engine(database_location)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
    def create_company(self,symbol):
        temp_company = Company(symbol='GOOG')
        self.session.add(temp_company)
        self.session.commit()
    

