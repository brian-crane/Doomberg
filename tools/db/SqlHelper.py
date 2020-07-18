"""
This class helps me format SQL messages for use by DbTools
"""
from tools.other import Time as T

#format for adding a stock to a users portfolio
def updateStockPortfolioSQL(userId, portfolioId, symbol, quanity):
    return "INSERT INTO users.portfolio (\"portfolio_id\", \"user_id\", \"symbol\", \"quantity\",\"created_ts\",\"modified_ts\") VALUES ('"+str(portfolioId)+"', '"+str(userId)+"', '"+str(symbol)+"', '"+str(quanity)+"','"+T.getSqlTime()+"','"+T.getSqlTime()+"');"

#add stock price to stocks.price
def insertSymbolPriceSQL(symbol, price, priceTs, isAfterHours, source):
    return "INSERT INTO stocks.price (\"symbol\", \"price\", \"price_ts\",\"after_hours\",\"source\",\"created_ts\",\"modified_ts\") VALUES ('"+str(symbol)+"', '"+str(price)+"', '"+str(priceTs)+"',"+str(isAfterHours)+",'"+source+"','"+T.getSqlTime()+"','"+T.getSqlTime()+"');"

