import yfinance as yf

# Return the USD price of current stock Right Now
def getCurrentStockPrice(symbol):
    msft = yf.Ticker(symbol)
    return "WAIT YFINANCE IS ONLY FOR HISTORICAL STOCK PRICES"