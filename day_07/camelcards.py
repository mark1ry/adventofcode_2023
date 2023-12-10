import numpy as np
from classes import Hand, Play
                
def read_input(dir: str) -> list:
    input = []
    with open(dir, "r") as file:
        for line in file:
            hand, bid = line.split()
            input.append(Play(hand, bid))
    return input

def find_type_strength(string):
    match string:
        case "Pair":
            return 1
        case "Double pair":
            return 2
        case "Trio":
            return 3
        case "Full house":
            return 4
        case "Poker":
            return 5
        case "Repoker":
            return 6
        case "High card":
            return 0
               
def order_value(play):
    value = 0
    print(play.hand.hand)
    value += find_type_strength(play.hand.type) * pow(10, 10)
    relative_strength = 8
    for element in play.hand.strength:
        value += element*pow(10, relative_strength)
        relative_strength -= 2
    return value

def camel_cards():
    input = read_input("/home/marc/Programming/advent_calendar/day_7/camelcards_input.txt")
    input.sort(key=order_value)
    result = 0
    for index, element in enumerate(input):
        print(element.hand.hand)
        result += element.bid * (index+1)
    print(f"The total winnings are {result}")

if __name__ == "__main__":
    camel_cards()