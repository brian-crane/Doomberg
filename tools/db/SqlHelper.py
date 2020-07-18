"""
This class helps me format SQL messages for use by DbTools
"""
from tools.other import Time as T

#format for adding a stock to a users portfolio
def updateStockPortfolioSQL(userId, symbol, quanity):
    return "INSERT INTO users.portfolio (\"user_id\", \"symbol\", \"quantity\") VALUES ('"+str(userId)+"', '"+str(symbol)+"', '"+str(quanity)+");"

#add stock price to stocks.price
def insertSymbolPriceSQL(symbol, price, priceTs, isAfterHours, source):
    return "INSERT INTO stocks.price (\"symbol\", \"price\", \"price_ts\",\"after_hours\",\"source\") VALUES ('"+str(symbol)+"', '"+str(price)+"', '"+str(priceTs)+"',"+str(isAfterHours)+",'"+source+"');"

