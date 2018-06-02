import sys
from src.errorExit import *

def 	convertData(readBuffer):
    res = readBuffer.split("\n")
    listRes = list()
    for x in res:
        tmp = x.split(",")
        try :
            listRes.append([float(tmp[0]), float(tmp[1])])
        except:
           pass
    if (len(listRes)) < 2:
    	errorExit("Error data")
    return listRes