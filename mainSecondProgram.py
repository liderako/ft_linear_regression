import sys
from math import *
import math
from src.readFile import readFile
from src.convertData import convertData
from src.errorExit import *
from src.calcEstimatedPrice import *
from src.writeFile import *

if (len(sys.argv) != 2):
    errorExit("Usage: python main.py fileData")

def min_max_scaling(data):
    X = [_[0] for _ in data]
    y = [_[1] for _ in data]
    minX = min(X)
    maxX = max(X)
    for i in range(len(X)):
        data[i][0] = (X[i] - minX) / (maxX - minX)
    return data

data = convertData(readFile(sys.argv[1]))

learningRate = 0.1

teta0 = 0.0
teta1 = 0.0
m = float(len(data))
data = min_max_scaling(data)
print(data)
cnt = 0
while True:
    cnt += 1
    sumOne = 0
    sumTwo = 0
    for x in data:
        km = float(x[0])
        price = float(x[1])
        sumOne += (calcEstimatedPrice(km, teta0, teta1) - price)
        sumTwo += ((calcEstimatedPrice(km, teta0, teta1) - price) * km)
    # print("{} - {} * {}".format(teta0, learningRate, grad_teta0))
    # print("{} - {} * {}".format(teta1, learningRate, grad_teta1))
    new_teta0 = teta0 - learningRate * (sumOne / m)
    new_teta1 = teta1 - learningRate * (sumTwo / m)
    print(new_teta0, new_teta1)

    # print ("sum, ", sumOne, sumTwo, learningRate)
    # new_teta0 = learningRate * (sumOne / float(m))
    # new_teta1 = learningRate * (sumTwo / float(m))
    if teta0 == new_teta0 and teta1 == new_teta1:
        break
    teta0 = new_teta0
    teta1 = new_teta1
    if cnt >= 2000:
        break
print (teta0, teta1)
writeFile(teta0, teta1)
