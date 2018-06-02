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

data = convertData(readFile(sys.argv[1]))

learningRate = 0.0001

teta0 = 0.0
teta1 = 0.0
m = float(len(data))

sumOne = 0
sumTwo = 0
for x in data:
    km = float(x[0])
    price = float(x[1])
    sumOne += (calcEstimatedPrice(km, teta0, teta1) - price)
    sumTwo += ((calcEstimatedPrice(km, teta0, teta1) - price) * km)
teta0 = learningRate * (sumOne / float(m))
teta0 = learningRate * (sumTwo / float(m))
print (teta0, teta1)
writeFile(teta0, teta1)