
def read_input(dir: str) -> list:
    with open(dir, "r") as file:
        return [list(line.replace("\n", "")) for line in file]

def convert_sketch(sketch: str):
    pipes = []
    for list in sketch:
        current = []
        for element in list:
            match element:
                case ".":
                    current.append("")
                case "-":
                    current.append("eastwest")
                case "|":
                    current.append("northsouth")
                case "L":
                    current.append("northeast")
                case "J":
                    current.append("northwest")
                case "F":
                    current.append("eastsouth")
                case "7":
                    current.append("westsouth") 
                case "S":
                    current.append("start")
        pipes.append(current)
    return pipes

def find_start(pipes):
    for row in range(len(pipes)):
        for column in range(len(pipes[row])):
            if pipes[row][column] == "start":
                return [row, column]

def find_paths(start, pipes):
    paths = []
    if start[0]!=0:
        if "south" in pipes[start[0]-1][start[1]]:
            paths.append("north")
    if start[0]!=(len(pipes)-1):
        if "north" in pipes[start[0]+1][start[1]]:
            paths.append("south")
    if start[1]!=0:
        if "east" in pipes[start[0]][start[1]-1]:
            paths.append("west")
    if start[1]!=(len(pipes[0])-1):
        if "west" in pipes[start[0]][start[1]+1]:
            paths.append("east")
    return paths

def go_north(current_coord: list, pipes) -> list:
    pipes[current_coord[0]-1][current_coord[1]] = pipes[current_coord[0]-1][current_coord[1]].replace("south", "")
    return [current_coord[0]-1, current_coord[1]]

def go_south(current_coord: list, pipes) -> list:
    pipes[current_coord[0]+1][current_coord[1]] = pipes[current_coord[0]+1][current_coord[1]].replace("north", "")
    return [current_coord[0]+1, current_coord[1]]

def go_west(current_coord: list, pipes) -> list:
    pipes[current_coord[0]][current_coord[1]-1] = pipes[current_coord[0]][current_coord[1]-1].replace("east", "")
    return [current_coord[0], current_coord[1]-1]

def go_east(current_coord: list, pipes) -> list:
    pipes[current_coord[0]][current_coord[1]+1] = pipes[current_coord[0]][current_coord[1]+1].replace("west", "")
    return [current_coord[0], current_coord[1]+1]

def move_next(pipe_sketch: list):
    pipes = convert_sketch(pipe_sketch)
    start_coordinates = find_start(pipes)
    possible_paths = find_paths(start_coordinates, pipes)
    sketch = [["." for element in line ] for line in pipe_sketch]
    for path in possible_paths:
        current_coord = start_coordinates
        sketch[current_coord[0]][current_coord[1]] = "X"
        pipes = convert_sketch(pipe_sketch)
        match path:
            case "north":
                current_coord=go_north(current_coord, pipes)
            case "south":
                current_coord=go_south(current_coord, pipes)
            case "east":
                current_coord=go_east(current_coord, pipes)
            case "west":
                current_coord=go_west(current_coord, pipes)
        step = 1
        while(current_coord!=start_coordinates):
            sketch[current_coord[0]][current_coord[1]] = "X"
            match pipes[current_coord[0]][current_coord[1]]:
                case "north":
                    current_coord=go_north(current_coord, pipes)
                case "south":
                    current_coord=go_south(current_coord, pipes)
                case "east":
                    current_coord=go_east(current_coord, pipes)
                case "west":
                    current_coord=go_west(current_coord, pipes)
            step += 1
    return sketch

def print_results(result):
    for line in result:
        for element in line:
            print(element, end=" ")
        print("\n", end="")
    print("\n", end="")

def find_maximum(sketch):
    maximum = 0
    for row in sketch:
        for element in row:
            maximum = element if element>maximum else maximum
    return maximum

def check_if_border(sketch, initial_row, initial_column):
    columns = [initial_column+value for value in range(-1,2) if -1<initial_column+value<len(sketch[0])]
    rows = [initial_row+value for value in range(-1,2) if -1<initial_row+value<len(sketch)]
    for row in rows:
        for column in columns:
            if(sketch[row][column]=="o"):
                sketch[initial_row][initial_column] = "o"
                return True
    return False
            
def find_borders(sketch):
    for line in sketch:
        index = 0
        while(index<len(line) and line[index]!="X"):
            line[index] = "o" 
            index += 1
        index = len(line)-1
        while(index>-1 and line[index]!="X"):
            line[index] = "o"
            index -= 1
    progress = True
    
    for column in range(len(sketch[0])):
        index = 0
        while(index<len(sketch) and sketch[index][column]!="X"):
            sketch[index][column] = "o"
            index += 1
        index = len(sketch)-1
        while(index>-1 and sketch[index][column]!="X"):
            sketch[index][column] = "o"
            index -= 1    
    while (progress):
        progress = False
        for row in range(len(sketch)):
            for column in range(len(sketch[row])):
                if sketch[row][column]==".":
                    progress = True if check_if_border(sketch, row, column) else progress

def check_horizontal(sketch, row, column):
    left = sketch[row][column]
    right = sketch[row][column+1]
    if((left=="L" or left=="F" or left=="-" or left=="S") and (right=="J" or right=="7" or right=="-" or right=="S")):
        return "-"
    return "."

def check_vertical(sketch, row, column):
    top = sketch[row][column]
    bottom = sketch[row+1][column]
    if((top=="7" or top=="F" or top=="|" or top=="S") and (bottom=="J" or bottom=="L" or bottom=="|" or bottom=="S")):
        return "|"
    return "."

def extend_sketch(sketch):
    extended_sketch = [["%" for element in range(2*len(sketch[0])-1)] for line in range(2*len(sketch)-1)]
    for row in range(len(sketch)):
        for column in range(len(sketch[row])):
            extended_sketch[2*row][2*column] = sketch[row][column]
    for row in range(len(sketch)-1):
        for column in range(len(sketch[row])-1):
            extended_sketch[1+2*row][1+2*column] = "."
    for row in range(len(sketch)):
        for column in range(len(sketch[row])-1):
            extended_sketch[2*row][1+2*column] = check_horizontal(sketch, row, column)
    for row in range(len(sketch)-1):
        for column in range(len(sketch[row])):
            extended_sketch[1+2*row][2*column] = check_vertical(sketch, row, column)
    return extended_sketch    

def contract_sketch(sketch):
    contracted = [["%" for element in range(int((len(sketch[0])+1)/2))] for line in range(int((len(sketch)+1)/2))]
    for row in range(len(contracted)):
        for column in range(len(contracted[row])):
            contracted[row][column] = sketch[2*row][2*column]
    return contracted

def find_result(sketch):
    inside_loop = [[1 if element=="." else 0 for element in line] for line in sketch]
    result = 0
    for line in inside_loop:
        for element in line:
            result += element
    return result
                      
def pipes():
    sketch = read_input("/home/marc/Programming/advent_calendar/day_10/pipe_input.txt")
    extended_sketch = extend_sketch(sketch)
    sketch = move_next(extended_sketch)
    find_borders(sketch)
    contracted = contract_sketch(sketch)
    print_results(contracted)
    print(f"The area inside the loop is {find_result(contracted)}")
    
if __name__ == "__main__":
    pipes()