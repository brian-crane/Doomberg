from tools.db import DbTools as DB
from tools.db import SqlHelper
from tools.db.helpers import DbHelper
from tools.other import Time as T

debug = True

def getUserInfo(userId):
    try:
        value = DbHelper.select("Select * from users.user where user_id = " + str(userId))
    except Exception as e:
        value = "ERROR! -> " + str(e)
    return value

#Get all users in system
def getAllUserIds():
    return DbHelper.select("SELECT user_id from users.user ORDER BY user_id ASC")
