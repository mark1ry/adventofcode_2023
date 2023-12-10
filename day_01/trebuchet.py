import numpy as np

def ConvertToDigits(line: str) -> str:
    line = line.replace("one", "one1one") if "one" in line else line
    line = line.replace("two", "two2two") if "two" in line else line
    line = line.replace("three", "three3three") if "three" in line else line
    line = line.replace("four", "four4four") if "four" in line else line
    line = line.replace("five", "five5five") if "five" in line else line
    line = line.replace("six", "six6six") if "six" in line else line
    line = line.replace("seven", "seven7seven") if "seven" in line else line
    line = line.replace("eight", "eight8eight") if "eight" in line else line
    line = line.replace("nine", "nine9nine") if "nine" in line else line
    return line
    
def GetFirstDigit(line: str) -> int:
    for index in range(len(line)):
        if line[index].isnumeric():
            return int(line[index])

def GetLastDigit(line: str) -> int:
    length = len(line)
    for temp in range(length):
        index = length - temp - 1
        if line[index].isnumeric():
            return int(line[index])

def GetCalibrationValues(input) -> np.array:
    calibrationValues = np.array([], dtype=int)
    for line in input:
        line = ConvertToDigits(line)
        currentValue = (GetFirstDigit(line)*10) + GetLastDigit(line)
        calibrationValues = np.append(calibrationValues, currentValue)
    return calibrationValues

def GetResult():
    input = open("trebuchet_input.txt", "r")
    calibrationValues = GetCalibrationValues(input)
    print(np.sum(calibrationValues))

if __name__ == "__main__":
    GetResult()
