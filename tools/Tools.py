"""
This is for generic tools
"""

#Create a hash to identify a timestamp as already existing in DB
def hashTimestamp(timestamp):
    myHash = 0
    flip = -1
    count = 0
    for c in timestamp:
        count += ord(c) % 4
        if ord(c) % count==0: flip *= -1
        myHash += ord(c)*flip + ord(c)*count+myHash
    return myHash
