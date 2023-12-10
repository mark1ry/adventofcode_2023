def ClimbTheStairs():
    input = open("puzzle_input.txt", "r")
    line = input.readline()
    currentFloor = int(0)
    firstTime = True
    for index in range(len(line)):
        currentFloor += 1 if line[index] == "(" else 0
        currentFloor -= 1 if line[index] == ")" else 0
        if currentFloor==-1 and firstTime:
            print(f"The first character that causes Santa to enter the basement is {index+1}\n")
            firstTime = False
    print(f"The final destination for Santa is floor number {currentFloor}")
    
if __name__ == "__main__":
    ClimbTheStairs()