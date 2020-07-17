
import time

debug = True

def getTime():
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    return str(month)+"/"+str(day)+"/"+str(year)+" "+str(hour)+":"+str(min)