"""
This class helps me format SQL messages for use by DbTools
"""

#format for adding a stock to a users portfolio
def updateStockPortfolioSQL(userId, portfolioId, symbol, quanity):
    return "INSERT INTO users.portfolio (\"portfolio_id\", \"user_id\", \"symbol\", \"quantity\",\"created_ts\",\"modified_ts\") VALUES ('"+str(portfolioId)+"', '"+str(userId)+"', '"+str(symbol)+"', '"+str(quanity)+"',now(),now());"

#add stock price to stocks.price
def insertSymbolPriceSQL(symbol, price, priceTs, isMarketOpen):
    return "INSERT INTO stocks.price (\"symbol\", \"price\", \"price_ts\",\"is_market_open\",\"created_ts\",\"modified_ts\") VALUES ('"+str(symbol)+"', '"+str(price)+"', '"+str(priceTs)+"',"+str(isMarketOpen)+",now(),now());"