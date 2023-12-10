import numpy as np 

def read_input(dir: str) -> list:
    input = []
    with open(dir, "r") as file:
        for line in file:
            line = line.split()
            input.append([int(value) for value in line])
    return input

def find_differences(initial: list) -> list:
    return [initial[index+1] - initial[index] for index in range(len(initial)-1)]

def is_zero(values: list) -> bool:
    all_zeroes = True
    for value in values:
        if value!=0:
            all_zeroes=False
    return all_zeroes

def extrapolate(sequences: list) -> int:
    result = 0
    for index in range(len(sequences)):
        result = result + sequences[index][0] if index%2==0 else result - sequences[index][0]
    return result
    
def find_next(initial: list) -> int:
    current = initial
    sequences = []
    while(not is_zero(current)):
        sequences.append(current)
        current = find_differences(current)
    return extrapolate(sequences)   
        
def oasis():
    input = read_input("/home/marc/Programming/advent_calendar/day_09/oasis_input.txt")
    results = [find_next(sequence) for sequence in input]
    print(f"\nThe sum of the extrapolated values is {np.sum(results)}\n")
            
if __name__ == "__main__":
    oasis()