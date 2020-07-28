
from tools.db import DbTools
from tools.db.helpers import DbPortfolioHelper
from tools.db.helpers import DbUserHelper

debug = True

def getSymbolDictForFrontEndUse():
    myList = []
    for symbol in DbPortfolioHelper.getPortfolioStockList():
        myList.append({"label": symbol, "value": symbol})
    for user in DbUserHelper.getAllUserIds():
        myList.append({"label": "User " + str(user)+"'s Net Worth", "value": "User " + str(user)+"'s Net Worth"})
    return myList

#helper method to run select query
def select(query):
    records = DbTools.executeQuery(query)
    newRecords = []
    for r in records:
        value = str(r[0])
        i = 1
        while len(r) > i:
            value += ","+str(r[i])
            i+=1
        newRecords.append(value)
    return newRecords

