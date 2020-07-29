from tools.db import DbTools as DB
from tools.db import SqlHelper
from tools.db.helpers import DbHelper, DbPortfolioHelper, DbUserHelper, DbStockPriceHelper

debug = True

def dupCheckNetWorth(userId,netWorth,netWorthTs):
    query = "select * from users.net_worth where user_id = " +str(userId)+" and net_worth = "+str(netWorth)+" and ('"+str(netWorthTs)+"' - net_worth_ts) < '01:00:00'"
    records = DB.executeQuery(query)
    if len(records) > 0:
        return True
    return False


def getNetWorthTsForUser(userId):
    symbolList = DbPortfolioHelper.getPortfolioStockListForUser(userId)
    return DbHelper.select("select price_ts from stocks.price where symbol in("+str(symbolList).replace("[","").replace("]","")+") ORDER BY price_ts desc LIMIT 1")[0]

def getUserNetWorth(userId):
    try:
        value = DbHelper.select("select net_worth from users.net_worth where user_id = "+ str(userId) + "ORDER BY net_worth_ts DESC LIMIT 1")
    except Exception as e:
        value = "ERROR! -> " + str(e)
    return float(value)

def insertNewNetWorth(userId, netWorth, netWorthTs):
    if not dupCheckNetWorth(userId,netWorth,netWorthTs):
        DB.executeQuery(SqlHelper.insertNetWorthSql(userId,netWorth,netWorthTs))
    else:
        print("DUPLICATED NET WORTH! WE already have this one:\n\t" + str(userId) +", " + str(netWorth) +", " +netWorthTs)

#Returns all stocks for a user in form: [symbol, quantity]
def getNetWorthForUser(userId):
    records = DbHelper.select("SELECT symbol,quantity from Users.portfolio where user_id = " + str(userId))
    total = 0.0
    for record in records:
        myList = record.split(",")
        price = DbStockPriceHelper.getMostRecentPrice(myList[0])[0]
        value = float(price) * float(myList[1])
        total += value
    return round(total, 2)

#Calculates net_worth for ALL users and adds a new entry to Users.net_worth, with a timestamp
def calculateAndInsertNetWorthForAllUsers():
    for userId in DbUserHelper.getAllUserIds():
        netWorth = getNetWorthForUser(userId)
        if netWorth > 0:
            netWorthTs = getNetWorthTsForUser(userId)
            insertNewNetWorth(userId, netWorth,netWorthTs)
