"""
This is for generic tools, hashing algos, etc.
"""
import winsound


def playLowBeep():
    frequency = 100  # Set Frequency To 2500 Hertz
    duration = 991  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def playHighBeep():
    frequency = 180  # Set Frequency To 2500 Hertz
    duration = 991  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def playHigherBeep():
    frequency = 250  # Set Frequency To 2500 Hertz
    duration = 850  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)




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