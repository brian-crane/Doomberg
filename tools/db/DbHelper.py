"""
This class uses DBTools to call common queries
"""

from tools.db import DbTools as DB
from tools.db import SqlHelper as SH

debug = True

#Returns all stocks in portfolios, NO DUPLICATES
def getPortfolioStockList():
    records = DB.executeQuery("SELECT DISTINCT(symbol) from users.portfolio")
    newRecords = []
    for r in records:
        newRecords.append(r[0])
    return newRecords

#Returns true if a stock price has already registed in DB
def dupCheckStockPrice(myDict):
    symbol = myDict.get("symbol")
    price = myDict.get("price")
    priceTs = myDict.get("priceTs")
    query = "SELECT * FROM Stocks.price where symbol = '"+str(symbol)+"' and price = "+str(price)+" and price_ts = '"+str(priceTs)+"'"
    records = DB.executeQuery(query)
    if len(records) > 0:
        return True
    return False

def insertStockPrice(myDict):
    if myDict is None:
        if debug: print("given None as argument, skipping insertion")
        return
    symbol = myDict.get("symbol")
    price = myDict.get("price")
    priceTs = myDict.get("priceTs")
    isAfterHours = myDict.get("isAfterHours")
    source = myDict.get("source")
    if not dupCheckStockPrice(myDict):
        DB.executeQuery(SH.insertSymbolPriceSQL(symbol,price,priceTs,isAfterHours,source))
    else:
        if debug: print("\tDUPLICATE We already have this:\n\t\t " + str(myDict))

