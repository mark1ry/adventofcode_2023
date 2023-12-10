import numpy as np

def ReadInput(dir: str) -> list:
    file = open(dir, 'r')
    inputCards = []
    for line in file:
        winningNumbers = []
        yourNumbers = []
        currentCard = []
        line = line.split(":")
        inputWinningNumbers, inputYourNumbers = line[1].split("|", maxsplit=1)
        inputWinningNumbers = inputWinningNumbers.split()
        inputYourNumbers = inputYourNumbers.split()
        for number in inputWinningNumbers:
            winningNumbers.append(int(number))
        for number in inputYourNumbers:
            yourNumbers.append(int(number))
        currentCard.append(winningNumbers)
        currentCard.append(yourNumbers)
        inputCards.append(currentCard)
    return inputCards


def GetValues(cards: list) -> list:
    cardsValue = []
    for card in cards:
        currentValue = 0
        for yourNumber in card[1]:
            if yourNumber in card[0]:
                currentValue = 2*currentValue if currentValue!=0 else 1
        cardsValue.append(currentValue)
    return cardsValue

def multiplyCards(cards: list) -> list:
    cardsQuantity = [1 for dummy in range(len(cards))]
    for index in range(len(cards)):
        currentMatches = 0
        for yourNumber in cards[index][1]:
            if yourNumber in cards[index][0]:
                currentMatches+=1
        for match in range(currentMatches):
            cardsQuantity[index+match+1] += cardsQuantity[index]
    return cardsQuantity

def Scratchcards():
    scratchCards = ReadInput("/home/marc/Programming/advent_calendar/day_4/cards_input.txt")
    cardsValue = GetValues(scratchCards)
    numberOfCards = multiplyCards(scratchCards)
    print(f"\nThe total value of the cards is {np.sum(cardsValue)}\n")
    print(f"The total number of scratch cards is {np.sum(numberOfCards)}\n")
    
if __name__ == "__main__":
    Scratchcards()
        