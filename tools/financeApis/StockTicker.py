import datetime
import urllib

import requests
import json

from tools.other import Time as T

debug = True

def getIEXCloudData(symbol):
    url = "https://cloud.iexapis.com/stable/stock/"+symbol+"/batch?types=quote&token=pk_d972831e3b8e4aa38b9e138a7d59aa01"
    response = requests.get(url)
    if debug: print(url)
    data = str(response.content)
    if response.status_code != 200:
        if debug: print("\t\tERROR, statusCode: " + str(response.status_code) +"\n\tmessage: " + data)
        return None
    data = data[2:len(data)-1]
    data = json.loads(data)

    price = data.get("quote").get("latestPrice")
    priceTs = data.get("quote").get("latestUpdate")
    priceTs = datetime.datetime.fromtimestamp(float(priceTs)/1000.)
    myDict = {"symbol":str(symbol),"price":str(price),"priceTs":str(priceTs)[0:str(priceTs).rindex(".")], "isAfterHours":False,"source":"IEXCloud"}
    if debug: print(myDict)
    return myDict


def getAfterHourDataCNN(symbol):
    url = "https://money.cnn.com/quote/quote.html?symb="+symbol
    if debug: print(url)
    response = urllib.request.urlopen(url)
    html = str(response.read())
    #streamFormat="ToHundredth" streamFeed="BatsUS">
    html = html[html.index("streamFormat=\"ToHundredth\" streamFeed=\"BatsUS\">"):]
    html = html[html.index(">")+1:]
    price = html[0:html.index("<")].replace(",","")
    try:
        html = html[html.index("streamDateFormat=\"h%3Aia%20x\">"):]
        html = html[html.index(">")+1:]
        priceTs = html[0:html.index("<")]

        hour = int(priceTs[0:1]) -3 #EST
        if "pm" in priceTs:
            hour += 12
        minute = int(priceTs[2:4])
        priceTs = datetime.datetime(T.getTimeInterval("year"), T.getTimeInterval("month"), T.getTimeInterval("day"), hour, minute)
    except ValueError as e:
        if debug: print("No specific time data avaialble")
        html = html[html.index("As of ")+6:]
        html = html[0:html.index("<")]
        month = html[0:html.index(" ")]
        month = T.parseMonth(month)
        day = int(html[html.index(" ")+1:])
        hour = 17
        minute = 0
        priceTs = datetime.datetime(T.getTimeInterval("year"), month, day, hour, minute)

    myDict = {"symbol":str(symbol),"price":str(price),"priceTs":str(priceTs), "isAfterHours":True,"source":"CNN Money"}
    if debug: print(myDict)
    return myDict

