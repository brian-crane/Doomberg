"""
This is for generic tools, hashing algos, etc.
"""

#Create a hash to identify a stock Dict as already existing in DB
def getStockHash(myDict):
    myHash = 0

    return myHash

def getMaxMinFromArray(myArray):
    min = 10000000.0
    max = 0.0
    for element in myArray:
        if float(element) > max: max = float(element)
        if float(element) < min: min = float(element)
    return {"max":max,"min":min}

def normalizeArray(array,maxMin):
    max = maxMin["max"]
    min = maxMin["min"]
    newArray = []
    for element in array:
        newVal = (float(element) - min) / (max - min)
        newArray.append(newVal)