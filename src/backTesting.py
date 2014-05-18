"""
This is the main backtesting module
It will:
- Connect to the database
- Query for stocks
- integrate with trading strategies


Robert Micatka
May 17th, 2014
"""




import backTestingDefinitions




user1 = backTestingDefinitions.user('bob','2000-01-01',100000,0.03)
user1.buy('ABL','2000-01-02', 25, 500)
user1.printData('2000-01-05') #this does not work yet




