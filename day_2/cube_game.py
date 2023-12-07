import numpy as np

def ReadInput(dir: str) -> list:
    file = open(dir, "r")
    games = []
    for line in file:
        line = line.replace(",", "")
        tempInput = line.split(":")
        revealedSets = tempInput[1].split(";")
        currentGame = []
        for set in revealedSets:
            words = set.split()
            currentSet = np.zeros((3), dtype=int)
            for iteration, color in np.ndenumerate(["red", "blue", "green"]):    
                if color in words:
                    index = words.index(color)
                    currentSet[iteration] = int(words[index-1])
            currentGame.append(currentSet)     
        games.append(currentGame)
    return games

def ValidateGames(games: list) -> list:
    validGames = []
    index = 1
    for game in games:
        valid = True
        for set in game:
            valid = False if set[0]>12 else valid
            valid = False if set[1]>14 else valid
            valid = False if set[2]>13 else valid
        if valid:
            validGames.append(index)
        index += 1
    return validGames

def FindMinimumCubes(games: list) -> list:
    minimumCubes = []
    for game in games:
        minRed = 0
        minBlue = 0
        minGreen = 0
        for set in game:
            minRed = set[0] if set[0]>minRed else minRed
            minBlue = set[1] if set[1]>minBlue else minBlue
            minGreen = set[2] if set[2]>minGreen else minGreen
        minimumCubes.append([minRed, minBlue, minGreen])
    return minimumCubes

def CalculatePower(minimumCubes: list) -> list:
    power = []
    for game in minimumCubes:
        power.append(game[0]*game[1]*game[2])
    return power
    
def CubeGame():
    games = ReadInput("/home/marc/Programming/advent_calendar/day_2/cube_game_input.txt")
    validGames = ValidateGames(games)
    minimumCubes = FindMinimumCubes(games)
    power = CalculatePower(minimumCubes)
    print(f"\nSum of the IDs is: {np.sum(validGames)}\n")
    print(f"The sum of the power of all games is: {np.sum(power)}\n")
    
if __name__ == "__main__":
    CubeGame()