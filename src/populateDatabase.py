"""
This will create and populate the database


Robert Micatka
May 7th, 2014
"""

import databaseDefinitions

test_data_base = databaseDefinitions('sqlite:///../../moiraiData/dailyStockPrice.db');

test_data_base.load_csv('../../moiraiData/infochimps_dataset_4776_download_16676/AMEX/test.csv')








