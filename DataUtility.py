

class Data:
    Name = ""
    Index = 0
    Datas = []

    def __init__(self, sName, sIndex, sDatas):
        self.Name = sName
        self.Index = sIndex
        self.Datas = sDatas


class DataRecord:
    Name = ""
    DataObjects = [Data]
    Indexes = 0

    def __init__(self, sName):
        self.name = sName
        self.DataObjects = []

    def createData(self, Name):
        self.DataObjects.append(Data(Name, self.Indexes, []))
        self.Indexes += 1

    def addData(self, NameToFind, data):
        for n in range(len(self.DataObjects)):
            if self.DataObjects[n].Name == NameToFind:
                return self.DataObjects[n].Datas.append(data)

        quit(str(self) + "Data not found: " + str(NameToFind))

    def find(self, NameToFind):
        for n in range(len(self.DataObjects)):
            if self.DataObjects[n].Name == NameToFind:
                return self.DataObjects[n].Datas

        quit(str(self) + "Data not found: " + str(NameToFind))

    def processData(self):
        for i in range(len(self.DataObjects[0].Datas)):
            for n in range(len(self.DataObjects)):
                if len(self.DataObjects[n].Datas) < i+1:  # Check if the data is empty
                    self.DataObjects[n].Datas.append(0.0)

    def parseFile(self, directory):
        file = open(directory, "r") # Read file

        # Parsing header names out and append data storate ------------------------------------------------------------------------------------------------------------------------------
        dataString = file.readline()  # Read first line of the file, so header names first

        k = 0
        for i in range(len(dataString)):  # Repeat for every character in the read datastring
            if dataString[i] == "," or dataString[i] == "\n":  # Cut string to up to the read section before the comma or return
                self.createData(str(dataString[k: i])) # Append dataname to the datanames list
                k = i + 1  # Set starting point of string to the next character that is not a comma or return

        # Parsing Data ------------------------------------------------------------------------------------------------------------------------------------------------------------------
        dataString = file.read()  # Read the next line, this time the first data string

        k = 0
        d = 0
        for i in range(len(dataString)):  # Repeat for the length of the read datastring
            if dataString[i] == "," or dataString[i] == "\n":  # Cut string to up to the read section before the comma or return
                self.DataObjects[d].Datas.append(float(dataString[k: i]))  # Append data to the 'd' data object to its Datas list
                k = i + 1  # Set starting point of string to the next character that is not a comma or return
                d += 1  # Move to the next data object
                if d > len(self.DataObjects) - 1:  # Set data object to find index to zero for the next line
                    d = 0

        file.close() # Close the file

    def createFile(self, directory):
        file = open(directory, "w") # Create new file

        for i in range(len(self.DataObjects)): # Write headers
            if i == len(self.DataObjects) - 1: # Check if the data header to write is the last one so to write a return rather than a comma separation
                file.write(self.DataObjects[i].Name + "\n")
            else:
                file.write(self.DataObjects[i].Name + ",")

        self.processData()

        for i in range(len(self.DataObjects[0].Datas)):
            for n in range(len(self.DataObjects)):
                if n == len(self.DataObjects) - 1:  # Check if the data to write is the last one so to write a return rather than a comma separation
                    file.write(str(round(self.DataObjects[n].Datas[i], 5)) + "\n")
                else:
                    file.write(str(round(self.DataObjects[n].Datas[i], 5)) + ",")

        file.close()

# TESTING ---------------------------------------------------------------------------------------------------------------------------------------------------------
'''
flightData = DataRecord("flightData#1", [])
flightData.parsefile("Parsing/FL575.CSV")

print(" ")
print("DataNames: ")
for i in range(len(flightData.DataObjects)):
    print(flightData.DataObjects[i].Name)

print(" ")
print("Data: ")
for i in range(len(flightData.DataObjects)):
    print(flightData.DataObjects[i].Datas)

flightData.createfile("Data Directory/FLTEST.CSV")
'''