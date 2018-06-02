import sys

def  minMaxScaling(n, minX, maxX):
    res = n
    try:
        res = ((n - minX) / (maxX - minX))
    except:
        pass
    return (res)