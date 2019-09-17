from Card import Card
import random

class Deck:
    __VALUES = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    __SUITS = ['H','S','C','D']

    def __init__(self):
        self.deck = []
        for i in self.__SUITS:
            for j in self.__VALUES:
                self.deck.append(Card(j,i))
        random.shuffle(self.deck)

        self.usedCards = []

    def shuffle(self):
        random.shuffle(self.deck)

    def giveOutHand(self):
        hand = self.deck.pop(),self.deck.pop()
        self.usedCards.append(hand[0])
        self.usedCards.append(hand[1])
        return hand

    def flop(self):
        pass

    def turn(self):
        pass

    def river(self):
        pass




myDeck = Deck()

print(myDeck.deck)

print(myDeck.deck.pop())

