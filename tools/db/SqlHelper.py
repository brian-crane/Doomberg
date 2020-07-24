"""
This class helps me format SQL messages for use by DbTools
"""
from tools.other import Time as T

def dupCheckStockPrice(myDict):
    symbol = myDict.get("symbol")
    price = myDict.get("price")
    priceTs = myDict.get("priceTs")
    return "SELECT * FROM Stocks.price where symbol = '"+str(symbol)+"' and price = "+str(price)+" and price_ts = '"+str(priceTs)+"'"

def insertNetWorthSql(userId,netWorth,netWorthTs):
    return "INSERT INTO users.net_worth (user_id, net_worth, net_worth_ts, created_ts, modified_ts) VALUES ('"+str(userId)+"', '"+str(netWorth)+"', '" + str(netWorthTs)+"', '"+T.getSqlTime()+"', '"+T.getSqlTime()+"');"

#format for adding a stock to a users portfolio
def updateStockPortfolioSQL(userId, symbol, quanity):
    return "INSERT INTO users.portfolio (\"user_id\", \"symbol\", \"quantity\", \"created_ts\",\"modified_ts\") VALUES ('"+str(userId)+"', '"+str(symbol)+"', '"+str(quanity)+"', '"+T.getSqlTime()+"', '"+T.getSqlTime()+"');"

#add stock price to stocks.price
def insertSymbolPriceSQL(myDict):
    symbol = myDict.get("symbol")
    price = round(float(myDict.get("price")),2)
    priceTs = myDict.get("priceTs")
    isAfterHours = myDict.get("isAfterHours")
    source = myDict.get("source")
    return "INSERT INTO stocks.price (\"symbol\", \"price\", \"price_ts\",\"after_hours\",\"source\", \"created_ts\",\"modified_ts\") VALUES ('"+str(symbol)+"', '"+str(price)+"', '"+str(priceTs)+"','"+str(isAfterHours)+"','"+source+"', '"+T.getSqlTime()+"', '"+T.getSqlTime()+"');"

