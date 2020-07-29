"""
This class is for methods related to the temporal
"""

import time

debug = True

def isTradingFloorOpen():
    return isAfterHourTradingOpen() or isMarketOpen()

def getDateOffset(dateStr):
    dateArr = dateStr.split(" ")
    dayOffset = 0
    hourOffset = 0
    if "day" in dateArr[0]:
        dayOffset = int(dateArr[1])
    if "hour" in dateArr[0]:
        hourOffset = int(dateArr[1])
    dateVal = str(getInterval("year"))+"-"+str(getInterval("month"))+"-"+str(int(getInterval("day"))+dayOffset)+" "
    dateVal += str(int(getInterval("hour"))+hourOffset)+":"+str(getInterval("min"))+":"+str(int(getInterval("second")))
    return dateVal

def toMins(hour, minute, amPm):
    hour = int(hour)
    minute = int(minute)
    value = 60*hour + minute
    if "pm" in amPm.lower():
        value += 12*60
    return value

def sleep(secs):
    print("sleeping for " + str(secs) + " seconds... (" + getTime()+")")
    limit = 60
    while secs > limit:
        time.sleep(limit)
        secs -= limit
        print("sleeping for " + str(secs) + " seconds... (" + getTime()+")")
    time.sleep(secs)

def isMarketOpen():
    hour, min = map(int, time.strftime("%H %M").split())
    if toMins(6, 30, "AM") < toMins(hour, min, "") < toMins(1, 00, "PM"): return True
    return False

def isAfterHourTradingOpen():
    hour, min = map(int, time.strftime("%H %M").split())
    if toMins(1, 00, "PM") < toMins(hour, min, "") < toMins(5, 30, "PM"): return True
    if toMins(1, 00, "AM") < toMins(hour, min, "") < toMins(6, 30, "AM"): return True
    return False

def getInterval(interval):
    year, month, day, hour, min, second = map(int, time.strftime("%Y %m %d %H %M %S").split())
    myDict = {"year":year,"month":month,"day":day,"min":min,"hour":hour,"second":second}
    return myDict.get(interval)

def getIntervalStr(interval):
    return str(getInterval(interval))

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
