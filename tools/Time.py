
import time

debug = True

#Return true if between 9:30 AM PST and 1:00 PM PST
def isMarketOpen():
    hour, min = map(int, time.strftime("%H %M").split())
    if hour*60+min > 9*60+30 and hour*60 + min < 13*60:
        if debug: print("Market is Open.")
        return True
    if debug: print("Market is Closed.")
    return False

def getTime():
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    return str(month)+"/"+str(day)+"/"+str(year)+" "+str(hour)+":"+str(min)