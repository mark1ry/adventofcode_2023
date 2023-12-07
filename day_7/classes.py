import numpy as np

class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.get_strength()
        self.get_type()
    
    def get_type(self):
        different_occurrances = []
        repetitions = []
        number_jokers = 0
        for strength in self.strength:
            if strength not in different_occurrances:
                different_occurrances.append(strength)
                if strength==1:
                    number_jokers = self.strength.count(strength)
                elif self.strength.count(strength)!=1:
                    repetitions.append(self.strength.count(strength))
        repetitions.sort()
        if number_jokers==5:
            repetitions = [5]
        elif repetitions==[] and number_jokers>0:
            repetitions.append(1+number_jokers)
        elif len(repetitions)>0:
            repetitions[-1] += number_jokers
        match repetitions:
            case []:
                self.type = "High card"
            case [2]:
                self.type = "Pair"
            case [3]:
                self.type = "Trio"
            case [2, 2]:
                self.type = "Double pair"
            case [2, 3]:
                self.type = "Full house"
            case [4]:
                self.type = "Poker"
            case [5]:
                self.type = "Repoker"            
    
    def get_strength(self):
        strength = []
        for index in range(len(self.hand)):
            match self.hand[index]:
                case "T":
                    strength.append(10)
                case "J":
                    strength.append(1)
                case "Q":
                    strength.append(11)
                case "K":
                    strength.append(12)
                case "A":
                    strength.append(13)
                case _:
                    strength.append(int(self.hand[index]))
        self.strength = strength
        
class Play():
    def __init__(self, hand, bid):
        self.hand = Hand(hand)
        self.bid = int(bid)