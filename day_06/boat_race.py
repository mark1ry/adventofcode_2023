import numpy as np

def ReadInput(dir: str) -> list:
    file = open(dir, "r")
    input = []
    for line in file:
        line = line.split(":")
        numbers = line[1].split()
        input.append([int(number) for number in numbers])
    return input

def CalculateDistance(stationaryTime, movingTime):
    return stationaryTime*movingTime

def FindThreshold(totalTime: int, minimumDistance: int):
    squareRoot = np.sqrt(totalTime*totalTime - 4*minimumDistance)
    return (totalTime-squareRoot)/2, (totalTime+squareRoot)/2

def ConvertInput(input):
    newValues = []
    for array in input:
        array = [str(element) for element in array]
        string = ""
        for element in array:
            string += element
        newValues.append(int(string))
    return newValues

def FindNumberSolutions(input: list) -> int:
    minTime, maxTime = FindThreshold(input[0], input[1])
    return int(np.floor(maxTime) - np.floor(minTime))

def FindHoldingTime(input: list):
    solutions = []
    for race in input:
        solutions.append(FindNumberSolutions(race))
    return solutions
                    
def BoatRace():
    input = ReadInput("/home/marc/Programming/advent_calendar/day_6/race_input.txt")
    inputFirstPart = zip(input[0], input[1])
    numberOfSolutions = FindHoldingTime(tuple(inputFirstPart))
    result = 1
    for race in numberOfSolutions:
        result *= race
    print(f"The product of the number of ways is: {result}")
    
    inputSecondPart = ConvertInput(input)
    result = FindNumberSolutions(inputSecondPart)
    print(f"The number of dolutions is {result}")

if __name__ == "__main__":
    BoatRace()    
