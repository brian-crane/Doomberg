"""
This class is for methods related to the temporal
"""

import time

debug = True

def timeToMins(hour, minute, amPm):
    value = 60*hour + minute
    if "pm" in amPm.lower():
        value += 12*60
    return value

def sleep(secs):
    print("sleeping for " + str(secs) + " seconds... (" + getTime()+")")
    time.sleep(secs)

def isMarketOpen():
    hour, min = map(int, time.strftime("%H %M").split())
    if timeToMins(6,30,"AM") < timeToMins(hour,min,"") < timeToMins(1,00,"PM"): return True
    return False

def isAfterHourTradingOpen():
    hour, min = map(int, time.strftime("%H %M").split())
    if timeToMins(1,00,"PM") < timeToMins(hour,min,"") < timeToMins(5,00,"PM"): return True
    if timeToMins(1,00,"AM") < timeToMins(hour,min,"") < timeToMins(6,30,"AM"): return True
    return False

def getTimeInterval(interval):
    year, month, day, hour, min, second = map(int, time.strftime("%Y %m %d %H %M %S").split())
    myDict = {"year":year,"month":month,"day":day,"min":min,"second":second}
    return myDict.get(interval)

def getSqlTime():
    year, month, day, hour, min, second = map(int, time.strftime("%Y %m %d %H %M %S").split())
    return str(year)+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(min)+":"+str(second)

def getTime():
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    return str(month)+"/"+str(day)+"/"+str(year)+" "+str(hour)+":"+str(min)

def parseMonth(month):
    month = month.lower()
    if "jan" in month: return 1
    if "feb" in month: return 2
    if "mar" in month: return 3
    if "apr" in month: return 4
    if "may" in month: return 5
    if "jun" in month: return 6
    if "jul" in month: return 7
    if "aug" in month: return 8
    if "sep" in month: return 9
    if "oct" in month: return 10
    if "nov" in month: return 11
    if "dec" in month: return 12
    return -1
