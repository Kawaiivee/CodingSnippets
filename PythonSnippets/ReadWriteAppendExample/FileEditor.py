fileName = "data.txt"
modeDict = {'r':'READ','w':'WRITE','a':'APPEND','r+':"READ+WRITE"}
print("Enter mode: ", modeDict)
fileMode = input()

while fileMode not in modeDict:
	print("Enter a valid mode: ", modeDict)
	fileMode = input()

print("Opening file in", modeDict[fileMode], "mode")

try:
	print("Trying to open file " + fileName)
	file = open(fileName, fileMode)
except:
	print("Error Opening File!")
	exit()
	
print("File open in", modeDict[fileMode], "mode success!")

def readFile():
	linesList = file.readlines()
	print("Whole File in a list is: ", linesList)
	for line in linesList:
		print(line)
	file.close()
	exit()
	
def writeFile():
	print("Start writing to file: ")
	while True:
		currentInput = input()
		if currentInput == "exit":
			file.close()
			print("Finished writing to file")
			exit()
		else:
			currentInput = currentInput + "\n"
			file.write(currentInput)

def appendFile():
	pass
	
def readWriteFile():
	pass

operationsDict = {'r': readFile, 'w':writeFile, 'a':appendFile, 'r+':readWriteFile}
operationsDict[fileMode]()
exit()