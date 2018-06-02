def writeFile(list):
	file = open("tetas.csv", "w")
	file.write("teta0,teta1\n")
	file.write(str(list[0]) + "," + str(list[1]) + "\n")
	file.write(str(list[2]) + "," + str(list[3]) + "\n")
	file.close()