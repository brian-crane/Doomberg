# The Purpose of this class is to:
# Update all stock prices in DB stocks.stocks
# Include all stocks that are included in at least ONE portfolio
# Include major index funds
# Run on a cron job cycle
# No outside API interaction planned at the moment

"""
1. Loop through all stocks in all user portfolios
2. For each stock get the current value and insert into tables
3. Wait for X minutes and do it again!
"""

from tools.financeApis import IEXCloud as IEX
from tools.db import DbTools as DB
from tools.db import SqlHelper as SH
from tools import Tools as TOOL

myList = {"NFLX","SPY","TSLA","GOOGL","MSFT","HACK","WFH"}

for symbol in myList:
    myDict = IEX.getCurrentStockPrice(symbol)
    DB.executeQuery(SH.insertSymbolPriceSQL(myDict.get("symbol"),myDict.get("price"),myDict.get("priceTs"),myDict.get("isMarketOpen")))

DB.closeConnection()
