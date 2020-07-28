from tools.db import DbTools as DB
from tools.db import SqlHelper
from tools.db.helpers import DbHelper
from tools.other import Time as T

debug = True

def getStockPriceOverTimeDateFilter(symbol, dateRange):
    if "net worth" in symbol.lower():
        userId = symbol[symbol.index(" ")+1:symbol.index("'")]
        return DbHelper.select("select net_worth from users.net_worth where user_id = "+userId+" and net_worth_ts > '"+dateRange+"'ORDER BY net_worth_ts DESC")
    return DbHelper.select("select price from stocks.price where symbol = '"+symbol+"' and price_ts > '"+dateRange+"'ORDER BY price_ts DESC")

def getStockPriceTsOverTimeDateFilter(symbol, dateRange):
    if "net worth" in symbol.lower():
        userId = symbol[symbol.index(" ")+1:symbol.index("'")]
        return DbHelper.select("select net_worth_ts from users.net_worth where user_id = "+userId+" and net_worth_ts > '"+dateRange+"' ORDER BY net_worth_ts DESC")
    return DbHelper.select("select price_ts from stocks.price where symbol = '"+symbol+"' and price_ts > '"+dateRange+"' ORDER BY price_ts DESC")

def getMostRecentPrice(symbol):
    return DbHelper.select("SELECT price from Stocks.price where symbol = '"+symbol+"' ORDER BY price_ts DESC LIMIT 1")

#Returns true if a stock price has already registed in DB
def dupCheckStockPrice(myDict):
    query = SqlHelper.dupCheckStockPrice(myDict)
    records = DB.executeQuery(query)
    if len(records) > 0:
        return True
    return False

def insertStockPrice(myDict):
    if myDict is None:
        if debug: print("given None as argument, skipping insertion")
        return
    if not dupCheckStockPrice(myDict):
        DB.executeQuery(SqlHelper.insertSymbolPriceSQL(myDict))
    else:
        if debug: print("\tDUPLICATE We already have this:\n\t\t " + str(myDict))

