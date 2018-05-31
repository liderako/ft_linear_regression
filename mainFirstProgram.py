import sys
from src.readFile import *
from src.errorExit import *
from src.convertData import *
from src.calcEstimatedPrice import *
from src.isInt import *

def 	convertMileage(s):
	mileage = 0
	try:
		isInt(s)
		mileage = int(s)
		if (mileage < 0):
			sys.exit(-1)
	except:
		errorExit("Invalid digitals mileage")
	return (mileage)

if (len(sys.argv) != 2):
	errorExit("Usage: python mainFirstProgram mileage")
mileage = convertMileage(sys.argv[1])

readBuffer = readFile("tetas.csv")
dataTetaList = convertData(readBuffer)
print (calcEstimatedPrice(mileage, dataTetaList[0][0], dataTetaList[0][1]))