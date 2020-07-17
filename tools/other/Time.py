
import time

debug = True

def isMarketOpen():
    hour, min = map(int, time.strftime("%H %M").split())
    if 9*60+30 < hour*60+min < 13*60:
        if debug: print("Market is Open.")
        return True
    if debug: print("Market is Closed.")
    return False

def isAfterHourTradingOpen():
    hour, min = map(int, time.strftime("%H %M").split())
    if 13*60 < hour*60+min < 17*60:
        if debug: print("After Hour trading is Open.")
        return True
    if debug: print("After Hour trading is Closed.")
    return False

def getTimeInterval(interval):
    year, month, day, hour, min, second = map(int, time.strftime("%Y %m %d %H %M %S").split())
    myDict = {"year":year,"month":month,"day":day,"min":min,"second":second}
    return myDict.get(interval)

def getTime():
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    return str(month)+"/"+str(day)+"/"+str(year)+" "+str(hour)+":"+str(min)