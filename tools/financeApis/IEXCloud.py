import datetime

import requests
import json

from tools import Time as T

debug = True

#This returns the current stock price, INCLUDING AFTER HOURS PRICE
def getCurrentStockPrice(symbol):
    url = "https://cloud.iexapis.com/stable/stock/"+symbol+"/batch?types=quote&token=pk_d972831e3b8e4aa38b9e138a7d59aa01"
    response = requests.get(url)
    if debug: print(url)
    data = str(response.content)
    data = data[2:len(data)-1]
    data = json.loads(data)
    isMarketOpen = data.get("quote").get("isUSMarketOpen")
    priceTs = data.get("quote").get("latestUpdate")
    price = data.get("quote").get("extendedPrice")
    if isMarketOpen or price is None:
        price = data.get("quote").get("latestPrice")
        priceTs = data.get("quote").get("extendedPriceTime")
        return price
    priceTs = datetime.datetime.fromtimestamp(float(priceTs)/1000.)
    myDict = {"symbol":str(symbol),"price":str(price),"priceTs":str(priceTs), "isMarketOpen":isMarketOpen}
    if debug: print(str(myDict))
    return myDict
