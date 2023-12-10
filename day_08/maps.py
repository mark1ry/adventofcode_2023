from math import lcm
from tqdm import tqdm

def read_input(dir: str) -> list:
    nodes = []
    with open(dir, "r") as file:
        counter = 0
        for line in file:
            if counter==0:
                instructions = line.replace("\n", "")
                counter+=1
                continue
            if line=="\n":
                counter+=1
                continue
            currentNode = []
            line = line.split("=")
            currentNode.append(line[0].strip())
            line = line[1].strip()
            line = line.strip("()\n").split(",")
            currentNode.append(line[0].strip())
            currentNode.append(line[1].strip())
            nodes.append(currentNode)
            counter+=1
    return instructions, nodes

def find_position(target_node: str, nodes: list) -> int:
    index = 0
    for node in nodes:
        if node[0]==target_node:
            return index
        index += 1

def find_initial_position(nodes: list) -> list:
    index = 0
    intial_positions = []
    for node in nodes:
        if node[0][-1]=="A":
            intial_positions.append(index)
        index += 1
    return  intial_positions

def print_nodes(positions: list, nodes: list):
    print("\nThe final nodes are: \n")
    for position in positions:
        print("    ", nodes[position][0])    
        
def follow_instructions(initial_node: list, nodes: list, instructions: str) -> list:
    output = []
    current_position = find_position(initial_node[0], nodes)
    target_indices = []
    for instruction_idx in range(len(instructions)):
        if nodes[current_position][0][-1]=="Z":
            target_indices.append(instruction_idx+1)
        new_node= nodes[current_position][1] if instructions[instruction_idx]=="L" else nodes[current_position][2]
        current_position = find_position(new_node, nodes)
        
    output.append(target_indices)
    output.append(current_position)
    return output

def find_cycle(initial_iteration: int, possible_iterations: list):
    current_position = initial_iteration
    found_a_loop = False
    past_values = []
    while (not found_a_loop):
        past_values.append(current_position)
        current_position = possible_iterations[current_position][-1]
        if current_position in past_values:
            index = past_values.index(current_position)
            cycle = past_values[index:]
            iterations_before_cycle = index
            found_a_loop = True
    return [cycle, iterations_before_cycle]

def get_targets(cycle, possible_iterations, instruction_length):
    targets = []
    for index in range(len(cycle[0])):
        for target in possible_iterations[cycle[0][index]][0]:
            targets.append(target + (index*instruction_length))
    start = instruction_length * cycle[1]
    cycle_length = len(cycle[0]) * instruction_length
    return [start, cycle_length, targets]

def find_common(first, second):
    max = lcm(first[1], second[1])
    results = [[], []]
    for index in tqdm(range(max//first[1]), desc="iterations", unit="intersection"):
        for target in first[2]:
            results[0].append(target + index*first[1])
    for index in tqdm(range(max//second[1]), desc="intersctions", unit="intersection"):
        for target in second[2]:
            results[1].append(target + index*second[1])
    intersection = [value for value in results[1] if value in results[0]]
    return [first[0], max, intersection]
    

def find_clash(cycles, possible_iterations, instruction_length):
    targets = [get_targets(cycle, possible_iterations, instruction_length) for cycle in cycles]
    print(targets)
    max = lcm(targets[0][1], targets[1][1], targets[2][1], targets[3][1], targets[4][1], targets[5][1])
    
    intersection1 = find_common(targets[0], targets[1])
    intersection2 = find_common(targets[2], targets[3])
    intersection3 = find_common(targets[4], targets[5])
    intersection4 = find_common(intersection1, intersection2)
    result = find_common(intersection4, intersection3)
    result = result[2][0]+result[0]-1
    return result
                
def read_maps():
    instructions, nodes = read_input("/home/marc/Programming/advent_calendar/day_8/maps_input.txt")
    possible_iterations = [follow_instructions(node, nodes, instructions) for node in nodes]
    initial_values = find_initial_position(nodes)
    cycles = [find_cycle(seed, possible_iterations) for seed in initial_values]
    results = find_clash(cycles, possible_iterations, len(instructions))
    print(results)

if __name__ == "__main__":
    read_maps()        
                