def writeFile(one, two):
	file = open("tetas.csv", "w")
	file.write("teta0,teta1\n")
	file.write(str(one) + "," + str(two))
	file.close()