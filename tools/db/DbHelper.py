"""
This class uses DBTools to call common queries
"""

from tools.db import DbTools as DB
from tools.db import SqlHelper as SH
from tools.other import Time as T

debug = True

def getUserNetWorth(userId):
    try:
        value = select("select net_worth from users.net_worth where user_id = "+ str(userId) + "ORDER BY net_worth_ts DESC LIMIT 1")
    except Exception as e:
        value = "ERROR! -> " + str(e)
    return float(value)


def getUserInfo(userId):
    try:
        value = select("Select * from users.user where user_id = " + str(userId))
    except Exception as e:
        value = "ERROR! -> " + str(e)
    return value

def insertNewNetWorth(userId, netWorth):
    DB.executeQuery("INSERT INTO users.net_worth (user_id, net_worth, net_worth_ts) VALUES ('"+str(userId)+"', '"+str(netWorth)+"', '"+T.getSqlTime()+"');")

def getMostRecentPrice(symbol):
    return select("SELECT price from Stocks.price where symbol = '"+symbol+"' ORDER BY price_ts DESC LIMIT 1")

#Returns all stocks for a user in form: [symbol, quantity]
def getNetWorthForUser(userId):
    records = select("SELECT symbol,quantity from Users.portfolio where user_id = " + str(userId))
    total = 0.0
    for record in records:
        myList = record.split(",")
        price = getMostRecentPrice(myList[0])[0]
        value = float(price) * float(myList[1])
        total += value
    return round(total, 2)

#Get all users in system
def getAllUserIds():
    return select("SELECT user_id from users.user ORDER BY user_id ASC")

#Calculates net_worth for ALL users and adds a new entry to Users.net_worth, with a timestamp
def calculateAndInsertNetWorthForAllUsers():
    for userId in getAllUserIds():
        netWorth = getNetWorthForUser(userId)
        if netWorth > 0: insertNewNetWorth(userId, netWorth)

#Returns all symbols in portfolios, NO DUPLICATES
def getPortfolioStockList():
    return select("SELECT DISTINCT(symbol) from users.portfolio")


#Returns true if a stock price has already registed in DB
def dupCheckStockPrice(myDict):
    symbol = myDict.get("symbol")
    price = myDict.get("price")
    priceTs = myDict.get("priceTs")
    query = "SELECT * FROM Stocks.price where symbol = '"+str(symbol)+"' and price = "+str(price)+" and price_ts = '"+str(priceTs)+"'"
    records = DB.executeQuery(query)
    if len(records) > 0:
        return True
    return False

def insertStockPrice(myDict):
    if myDict is None:
        if debug: print("given None as argument, skipping insertion")
        return
    symbol = myDict.get("symbol")
    price = myDict.get("price")
    priceTs = myDict.get("priceTs")
    isAfterHours = myDict.get("isAfterHours")
    source = myDict.get("source")
    if not dupCheckStockPrice(myDict):
        DB.executeQuery(SH.insertSymbolPriceSQL(symbol,price,priceTs,isAfterHours,source))
    else:
        if debug: print("\tDUPLICATE We already have this:\n\t\t " + str(myDict))

#helper method to run select query
def select(query):
    records = DB.executeQuery(query)
    newRecords = []
    for r in records:
        value = str(r[0])
        i = 1
        while len(r) > i:
            value += ","+str(r[i])
            i+=1
        newRecords.append(value)
    return newRecords

