import sys
from src.readFile import readFile
from src.convertData import convertData

if (len(sys.argv) != 2):
	print ("Usage: python main.py fileData")
	sys.exit(-1)
readBuffer = readFile(sys.argv[1])
resConvert = convertData(readBuffer)
