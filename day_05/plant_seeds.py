from tqdm import tqdm
from multiprocessing import Pool
from functools import partial


def ReadInput(dir: str) -> list:
    file = open(dir, "r")
    currentList = []
    list = []
    for line in file:
        if len(line)>1:
            currentList.append(line)
        else:
            list.append(currentList)
            currentList = []
    return list

def CleanInput(input: list) -> list:
    maps = []
    for index in range(len(input)):
        if index == 0:
            line = input[index][0].split(":")
            digits = line[1].split()
            seeds = [int(digits[i]) for i in range(len(digits))]
            maps.append(seeds)
        else:
            currentMap = []
            for line in input[index]:
                line = line.split()
                if len(line) == 3:
                    currentMap.append([int(line[i]) for i in range(3)])
            maps.append(currentMap)
    return maps

def MapToNext(element: int, map: list) -> int:    
    elementIsMapped = False
    for line in map:
        if element>=line[1] and element<(line[1]+line[2]):
            newValue = line[0]+(element-line[1])
            elementIsMapped = True
        if not elementIsMapped:
            newValue = element
    return newValue

def MapToPrevious(element: int, map: list) -> int:    
    elementIsMapped = False
    for line in map:
        if element>=line[0] and element<(line[0]+line[2]):
            newValue = line[1]+(element-line[0])
            elementIsMapped = True
        if not elementIsMapped:
            newValue = element
    return newValue

def FindMinimum(initialValue: int, dir: str) -> int:
    input = ReadInput(dir)
    maps = CleanInput(input)
    element = initialValue
    for index in range(len(maps)-1):
        element = MapToNext(element, maps[index+1])
    
    return element
            
def FindClosestLocation(maps: list, dir: str) -> int:
    seedRanges = [[maps[0][2*i+0], maps[0][2*i+1]] for i in range(len(maps[0])//2)]
    minimum = pow(10,10)
    for interval in seedRanges:
        initialValues = []
        for index in tqdm(range(interval[1]), desc="Finding initial seeds", unit="seed"):
            initialValues.append(interval[0]+index)
        with Pool() as pool:
            for result in pool.imap_unordered(partial(FindMinimum, dir=dir), initialValues, chunksize=50000):
                minimum = result if result<minimum else minimum
 
    return minimum

def FindSeed(initialValue, maps):
    length = len(maps)
    currentValue = initialValue
    for index in range(length-1):
        currentValue = MapToPrevious(currentValue, maps[length-1-index]) 
    return currentValue

def IsInList(seed: int, seedRanges: list) -> bool:
    for interval in seedRanges:
        if seed>=interval[0] and  seed<(interval[0]+interval[1]):
            return True
    return False

def FindClosestLocation(maps: list) -> int:
    seedRanges = [[maps[0][2*i+0], maps[0][2*i+1]] for i in range(len(maps[0])//2)]
    for element in tqdm(range(10000000), desc="Evaluation locations", unit="location"):
        seed = FindSeed(element, maps)
        if IsInList(seed, seedRanges):
            return element
    return -1
        
def PlantSeeds():
    path = "/home/marc/Programming/advent_calendar/day_5/maps_input.txt"
    input = ReadInput(path)
    maps = CleanInput(input)
    location = FindClosestLocation(maps)
    print(f"\nThe closest location is location {location}\n")
    
if __name__ == "__main__":
    PlantSeeds()