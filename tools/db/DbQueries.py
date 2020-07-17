"""
This class uses DBTools to call common queries
"""

from tools.db import DbTools as DB

#Returns true if a stock price has already registed in DB
def dupCheckStockPrice(symbol, price, time):
    symbol = "SPY"
    price = 320.79
    time = "2020-07-16 13:00:00.216"
    query = "SELECT * FROM Stocks.price where symbol = '"+str(symbol)+"' and price = "+str(price)+" and price_ts = '"+str(time)+"'"
    records = DB.executeQuery(query)
    if len(records) > 0:
        return True
    return False