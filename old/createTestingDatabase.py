"""
This file is simply for testing purposes, will not be used

Robert Micatka
May 6th, 2014

"""

import databaseDefinitions


new_database = databaseDefinitions.database('sqlite:///../data/company_testing.db')
new_database.add_company('MFST')

#new_daily_database = databaseDefinitions.database('sqlite:///../data/daily_testing.db')
new_database.add_daily_prices('MFST','2000-05-05','2014-05-05')






