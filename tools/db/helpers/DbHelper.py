
from tools.db import DbTools

debug = True

#helper method to run select query
def select(query):
    records = DbTools.executeQuery(query)
    newRecords = []
    for r in records:
        value = str(r[0])
        i = 1
        while len(r) > i:
            value += ","+str(r[i])
            i+=1
        newRecords.append(value)
    return newRecords

