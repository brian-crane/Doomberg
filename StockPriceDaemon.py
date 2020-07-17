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
make IRA account

Call Fidelity
Roll over account
Ask for check to mail to me
    -Make payable to Charles Schwab, FBO Brian Crane
    -Mail to Me

"""

from tools.financeApis import IEXCloud as IEX
from tools.db import DbTools as DB
from tools.db import SqlHelper as SH
from tools.db import DbQueries as DBQ

debug = True

myList = {"NFLX","SPY","TSLA","GOOGL","MSFT","HACK","WFH"}

for symbol in myList:
    myDict = IEX.getCurrentStockData(symbol)
    if not DBQ.dupCheckStockPrice(myDict.get("symbol"),myDict.get("price"),myDict.get("priceTs")):
        DB.executeQuery(SH.insertSymbolPriceSQL(myDict.get("symbol"),myDict.get("price"),myDict.get("priceTs"),myDict.get("isMarketOpen")))
    else:
        if debug: print("We already have " + myDict.get("symbol") + " at $" + myDict.get("price")+ " at " + myDict.get("priceTs"))

DB.closeConnection()
