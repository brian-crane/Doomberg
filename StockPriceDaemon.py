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
    -Mail to Me=

"""
from tools.db.helpers import DbPortfolioHelper, DbStockPriceHelper, DbNetWorthHelper
from tools.financeApis import StockTicker
from tools.db.helpers import DbHelper
from tools.other import Time

debug = True
alwaysGetDayPrice = True
alwaysgetAfterHoursPrice = True
sleepTimer = 1
loopTimer = 30

myList = DbPortfolioHelper.getPortfolioStockList()

while True:
    for symbol in myList:
        if Time.isMarketOpen() or alwaysGetDayPrice:
            DbStockPriceHelper.insertStockPrice(StockTicker.getIEXCloudData(symbol))
            sleepTimer = 1
            loopTimer = 30
        if Time.isAfterHourTradingOpen() or alwaysgetAfterHoursPrice:
            DbStockPriceHelper.insertStockPrice(StockTicker.getAfterHourDataCNN(symbol))
            sleepTimer = 5
            loopTimer = 600
        else: print("Markets are closed and so are my eyes! zzzzzzz.... " + Time.getTime())
        Time.sleep(sleepTimer)
    DbNetWorthHelper.calculateAndInsertNetWorthForAllUsers()
    Time.sleep(loopTimer)
