import sys
from math import *

import math
import matplotlib.pyplot as plt
from src.readFile import readFile
from src.convertData import convertData
from src.errorExit import *
from src.ft_math.calcEstimatedPrice import *
from src.ft_math.minMaxScaling import *
from src.writeFile import *

if (len(sys.argv) != 2):
    errorExit("Usage: python main.py fileData")

def minMaxScalingData(data):
    xList = list()
    for x in data:
        xList.append(x[0])
    minX = min(xList)
    maxX = max(xList)
    for i in range(len(xList)):
        data[i][0] = minMaxScaling(xList[i], minX, maxX)
    return (data, minX, maxX)

data = convertData(readFile(sys.argv[1]))

learningRate = 0.1
teta0 = 0.0
teta1 = 0.0
m = float(len(data))
data, maxX, minX = minMaxScalingData(data)
while True:
    sumOne = 0
    sumTwo = 0
    for x in data:
        km = float(x[0])
        price = float(x[1])
        sumOne += (calcEstimatedPrice(km, teta0, teta1) - price)
        sumTwo += ((calcEstimatedPrice(km, teta0, teta1) - price) * km)
    new_teta0 = teta0 - learningRate * (sumOne / m)
    new_teta1 = teta1 - learningRate * (sumTwo / m)
    if teta0 == new_teta0 and teta1 == new_teta1:
        break
    teta0 = new_teta0
    teta1 = new_teta1
writeFile([teta0, teta1, minX, maxX])