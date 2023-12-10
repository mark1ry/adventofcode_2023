import numpy as np

def GetInput(dir: str) -> np.array:
    file = open(dir)
    schemeLines = []
    for line in file:
        schemeLines.append(line[:-1])
    return schemeLines

def GetNumber(line: str, indicies: list) -> int:
    length = len(indicies)
    number = 0
    for position in range(length):
        number += int(line[indicies[position]]) * pow(10, length-position-1)
    return number

def IsSpecialCharacter(character: str) -> bool:
    if character!="." and not character.isnumeric():
        return True
    return False
 
def GetIndicesOfInterest(indices: list):
    indicesOfInterest = []
    indicesOfInterest.append(indices[0]-1)
    for index in indices:
        indicesOfInterest.append(index)
    indicesOfInterest.append(indices[-1]+1)
    return indicesOfInterest

def IsPartNumber(schemeLines: list, indices: list, lineIndex: int, numberLines: int, lineLength: int) -> bool:
    indexOfInterest = GetIndicesOfInterest(indices)
    isPartNumber = False
    for line in [lineIndex-1, lineIndex, lineIndex+1]:
        if line<0 or line==numberLines:
            continue
        for element in indexOfInterest:
            if element<0 or element==lineLength:
                continue
            isPartNumber = True if IsSpecialCharacter(schemeLines[line][element]) else isPartNumber
    return isPartNumber
                    
def FindPartNumbers(schemeLines: np.array) -> np.array:
    lineLength = len(schemeLines[0])
    numberLines = len(schemeLines)
    partNumbers = []
    lineIndex = 0
    for line in schemeLines:
        index = 0
        while index<lineLength:
            tempIndices = []
            while line[index].isnumeric():                
                tempIndices.append(index)
                if index==lineLength-1:
                    break
                index += 1
            if len(tempIndices)!=0:
                if IsPartNumber(schemeLines, tempIndices, lineIndex, numberLines, lineLength):
                    partNumbers.append(GetNumber(line, tempIndices))
            index += 1
        lineIndex += 1
    return partNumbers

def FindNumber(line: str, initialIndex: int) -> list:
    indices = [initialIndex,]
    index = initialIndex + 1 
    while index<len(line) and line[index].isnumeric():
        indices.append(index)
        index+=1
    index = initialIndex - 1
    while index>-1 and line[index].isnumeric():
        indices.append(index)
        index-=1
    indices = np.sort(indices)
    return indices

def IsInTheArray(indices: list, currentIndices: list) -> bool:
    for element in indices:
        if len(np.intersect1d(element,currentIndices))>0:
            return True
    return False
                    
def GetGear(schemeLines: list, lineIndex: int, position: int, lineLength: int, numberLines: int):
    indicesOfInterest = [position-1, position, position+1]
    linesOfInterest = [lineIndex-1, lineIndex, lineIndex+1]
    numbers = []
    for line in linesOfInterest:
        numberIndices = []
        for index in indicesOfInterest:
            if schemeLines[line][index].isnumeric():
                currentNumberIndices = FindNumber(schemeLines[line], index)
                if not IsInTheArray(numberIndices, currentNumberIndices):
                    numberIndices.append(currentNumberIndices)
                    numbers.append(GetNumber(schemeLines[line], currentNumberIndices))
    if len(numbers)==2:
        return numbers, True
    return [], False
                
def FindGears(schemeLines):
    lineLength = len(schemeLines[0])
    numberLines = len(schemeLines)
    gears = []
    for lineIndex in range(numberLines):
        for position in range(lineLength):
            if schemeLines[lineIndex][position]=="*":
                currentGear = GetGear(schemeLines, lineIndex, position, lineLength, numberLines)
                if currentGear[1]:
                    gears.append(currentGear[0])
    return gears

def GetGearRatios(schemeLines):
    gearNumbers = FindGears(schemeLines)
    gearRatios = []
    for gear in gearNumbers:
        gearRatios.append(gear[0]*gear[1])
    return gearRatios
    
def EngineSchematic():
    schemeLines = GetInput("/home/marc/Programming/advent_calendar/day_3/engine_input.txt")
    partNumbers = FindPartNumbers(schemeLines)
    gearRatios = GetGearRatios(schemeLines)
    print(f"\nThe sum of the part numbers is {np.sum(partNumbers)}\n")
    print(f"The sum of the gear ratios is {np.sum(gearRatios)}\n")

if __name__ == "__main__":
    EngineSchematic()