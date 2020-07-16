import requests
import json

from tools import Time as T

debug = True

#This returns the current stock price, INCLUDING AFTER HOURS PRICE
def getCurrentStockPrice(symbol):
    response = requests.get("https://cloud.iexapis.com/stable/stock/"+symbol+"/batch?types=quote&token=pk_d972831e3b8e4aa38b9e138a7d59aa01")
    data = str(response.content)
    data = data[2:len(data)-1]
    data = json.loads(data)
    if T.isMarketOpen():
        price = data.get("quote").get("latestPrice")
        if debug:
            print(symbol +" at " + T.getTime() +" is: " + price)
        return price
    price = data.get("quote").get("extendedPrice")
    print(symbol +" at " + T.getTime() +" is: " + str(price))
    return price