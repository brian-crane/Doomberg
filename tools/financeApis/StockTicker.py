import datetime
import urllib

import requests
import json

from tools.other import Time

debug = True

def getAfterHourDataYahooFinance(symbol):
    url ="https://finance.yahoo.com/quote/"+symbol
    if debug: print(">>> Getting Yahoo Finance Data for: " + symbol+"("+url+")")
    response = urllib.request.urlopen(url)
    html = str(response.read())
    if "After hours:<" not in html:
        if debug: print("No Yahoo Finance After Hours Data for: " + symbol)
        return None
    price = html[html.index("\"bid\":{\"raw\":")+13:]
    price = float(price[0:price.index(",")])
    priceTs = html[html.index("After hours:<"):]
    priceTs = priceTs[0:priceTs.index(" EDT")]
    priceTs = priceTs[priceTs.rindex(">")+1:]
    hour, min = int(priceTs.split(":")[0])-3, int(priceTs.split(":")[1].replace("PM",""))
    if "pm" in priceTs.lower():
        hour += 12
    priceTs = Time.getIntervalStr("month") +"-"+ Time.getIntervalStr("day") +"-"+ Time.getIntervalStr("year")+" "+str(hour) + ":" + str(min) +":00"
    myDict = {"symbol":str(symbol),"price":str(price),"priceTs":priceTs, "isAfterHours":True,"source":"Yahoo Finance"}
    if debug: print("YAHOO FINANCE DATA: " + str(myDict))
    return myDict

def getIEXCloudData(symbol):
    myDict = {}
    response = ""
    try:
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
    except Exception as e:
        if debug: print("ERROR GETTING DATA FROM IEX: "+ str(e)+"\nmyDict: "+ str(myDict) +"\n response = " + str(response))
        return None


def getAfterHourDataCNN(symbol):
    url = "https://money.cnn.com/quote/quote.html?symb="+symbol
    if debug: print(url)
    response = urllib.request.urlopen(url)
    html = str(response.read())
    htmlTemp = html[html.index("streamFormat=\"ToHundredth\" streamFeed=\"BatsUS\">"):]
    htmlTemp = htmlTemp[htmlTemp.index(">")+1:]
    price = htmlTemp[0:htmlTemp.index("<")].replace(",","")
    try:
        htmlDate = html[html.index("streamDateFormat=\"h%3Aia%20x\">"):]
        htmlDate = htmlDate[htmlDate.index(">")+1:]
        priceTs = htmlDate[0:htmlDate.index("<")]

        hour = int(priceTs[0:priceTs.index(":")]) -3 #EST
        if "pm" in priceTs:
            hour += 12
        minute = int(priceTs[priceTs.index(":")+1:priceTs.index(":")+3])
        priceTs = datetime.datetime(Time.getInterval("year"), Time.getInterval("month"), Time.getInterval("day"), hour, minute)
    except ValueError as e:
        if debug: print("No specific time data avaialble")
        html = html[html.index("As of ")+6:]
        html = html[0:html.index("<")]
        month = html[0:html.index(" ")]
        month = Time.parseMonth(month)
        day = int(html[html.index(" ")+1:])
        hour = 17
        minute = 0
        priceTs = datetime.datetime(Time.getInterval("year"), month, day, hour, minute)

    myDict = {"symbol":str(symbol),"price":str(price),"priceTs":str(priceTs), "isAfterHours":True,"source":"CNN Money"}
    if debug: print(myDict)
    return myDict

