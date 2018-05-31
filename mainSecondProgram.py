import sys
from src.readFile import readFile
from src.convertData import convertData
from src.errorExit import *

if (len(sys.argv) != 2):
	errorExit("Usage: python main.py fileData")

readBuffer = readFile(sys.argv[1])
resConvert = convertData(readBuffer)
