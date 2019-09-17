from Deck import Deck
from Player import Player
from Card import Card
from CLL import CircularList

class Game:

    def __init__(self):
        self.players = CircularList()
        self.players.add(Player(1500))
        self.players.add(Player(1300))
        self.players.add(Player(1600))
        self.players.add(Player(1700))

        self.deck = Deck()
        self.board = []

        self.bank =0
        self.diller = self.players.head.data
        self.sblind = 25
        self.bblind = 50



    def giveOutHands(self):


        for i in self.players.myList:
            i.setHand(self.deck.giveOutHand())


    def takeBlinds(self):
        if self.diller == len(self.players) - 1:
            self.bank += self.players[0].makeBet(self.sblind)
            self.bank += self.players[1].makeBet(self.bblind)
        elif self.diller == len(self.players) - 2:
            self.players[-1].makeBet(self.sblind)
            self.players[0].makeBet(self.bblind)
        else:
            self.bank += self.players[self.diller + 1].makeBet(self.sblind)
            self.bank += self.players[self.diller + 2].makeBet(self.bblind)
        self.bank += self.sblind + self.bblind

    def start(self):
        self.giveOutHands()
       # self.takeBlinds()

game = Game()

game.start()