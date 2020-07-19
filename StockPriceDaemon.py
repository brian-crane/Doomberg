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
import time
from tools.financeApis import StockTicker as ST
from tools.db import DbTools as DB
from tools.db import DbHelper
from tools.other import Time as T

debug = True
sleepTimer = 5
alwaysGetDayPrice = True
alwaysgetAfterHoursPrice = True
loopTimer = 10000 #5 minutes

myList = {"NVDA"}
myList = DbHelper.getPortfolioStockList()

while True:
    for symbol in myList:
        if T.isMarketOpen() or alwaysGetDayPrice:
            DbHelper.insertStockPrice(ST.getIEXCloudData(symbol))
        if T.isAfterHourTradingOpen() or alwaysgetAfterHoursPrice:
            DbHelper.insertStockPrice(ST.getAfterHourDataCNN(symbol))
        T.sleep(sleepTimer)
    DbHelper.calculateAndInsertNetWorthForAllUsers()
    T.sleep(loopTimer)
