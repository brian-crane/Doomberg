from tools.db import DbTools as DB
from tools.db import SqlHelper
from tools.db.helpers import DbHelper
from tools.other import Time as T

debug = True

#Returns all symbols in portfolios, NO DUPLICATES
def getPortfolioStockListForUser(userId):
    return DbHelper.select("SELECT DISTINCT(symbol) from users.portfolio where user_id = " + userId)

#Returns all symbols in portfolios, NO DUPLICATES
def getPortfolioStockList():
    return DbHelper.select("SELECT DISTINCT(symbol) from users.portfolio")
