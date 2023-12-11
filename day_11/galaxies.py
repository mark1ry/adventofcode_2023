import copy
import numpy as np

def read_input(dir: str) -> list:
    with open(dir, "r") as file:
        input = [list(line) for line in file]
    return input

def find_galaxies(chart: list) -> list:
    galaxies = []
    for row in range(len(chart)):
        for column in range(len(chart[row])):
            if chart[row][column]=="#":
                galaxies.append([row, column])
    return galaxies

def expand_universe(initial_distribution, chart):
    expansion = 999999
    new_distribution = copy.deepcopy(initial_distribution)
    for row in range(len(chart)):
        row_is_empty = True
        for index in range(len(initial_distribution)):
            row_is_empty = False if initial_distribution[index][0]==row else row_is_empty
        if row_is_empty:
            for index in range(len(initial_distribution)):
                new_distribution[index][0] = new_distribution[index][0]+expansion if initial_distribution[index][0]>row else new_distribution[index][0]
    for column in range(len(chart[0])):
        column_is_empty = True
        for index in range(len(initial_distribution)):
            column_is_empty = False if initial_distribution[index][1]==column else column_is_empty
        if column_is_empty:
            for index in range(len(initial_distribution)):
                new_distribution[index][1]= new_distribution[index][1]+expansion if initial_distribution[index][1]>column else new_distribution[index][1]
    return new_distribution

def get_distances(galaxies: list) -> list:
    distances = []
    number_of_galaxies = len(galaxies)
    for index_1 in range(number_of_galaxies):
        for index_2 in range(index_1+1, number_of_galaxies):
            distances.append(np.abs(galaxies[index_1][0]-galaxies[index_2][0]) + np.abs(galaxies[index_1][1]-galaxies[index_2][1]))
    return distances
            
def galaxies():
    chart = read_input("/home/marc/Programming/advent_calendar/day_11/galaxy_input.txt")
    galaxies = find_galaxies(chart=chart)
    galaxies = expand_universe(galaxies, chart)
    print(f"The sum of the distances is {np.sum(get_distances(galaxies))}")
    
if __name__ == "__main__":
    galaxies()
    