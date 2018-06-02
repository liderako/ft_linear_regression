import sys
from src.readFile import *
from src.errorExit import *
from src.convertData import *
from src.ft_math.calcEstimatedPrice import *
from src.ft_math.minMaxScaling import *
from src.isInt import *

def 	convertMileage(s, dataList):
	mileage = 0
	try:
		isInt(s)
		mileage = int(s)
		if (mileage < 0):
			sys.exit(-1)
	except:
		errorExit("Invalid digitals mileage")
	mileage = minMaxScaling(mileage, dataList[1][1], dataList[1][0])
	return (mileage)

if (len(sys.argv) != 2):
	errorExit("Usage: python mainFirstProgram mileage")

dataList = convertData(readFile("tetas.csv"))
mileage = convertMileage(sys.argv[1], dataList)
print (calcEstimatedPrice(mileage, float(dataList[0][0]), float(dataList[0][1])))