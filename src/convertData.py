import sys

def 	convertData(readBuffer):
    res = readBuffer.split("\n")
    listRes = list()
    for x in res:
        tmp = x.split(",")
        try :
            listRes.append([tmp[0], tmp[1]])
        except:
            pass
    listRes.pop(0)
    return listRes