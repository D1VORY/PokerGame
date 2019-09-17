class Player:

    def __init__(self,moneyBalance):
        self.moneyBalance = moneyBalance
        self.hand = None
        self.bet = 0
        self.isPlaying = True


    def setHand(self,hand):
        self.hand = hand

    def getHand(self):
        return self.hand

    def fold(self):
        self.hand = None

    def raiseBet(self, bet):
        self.bet = int(input("Raise from {} to {}".format(bet,self.moneyBalance)))
        while self.bet < bet or self.bet > self.moneyBalance:
            self.bet = int(input("Wrong Bet! It should be from {} to {}".format(bet, self.moneyBalance)))
        return self.bet

    def makeBet(self, bet=0):
        self.bet = bet
        return self.bet

    def call(self,bet):
        self.bet = bet

    def check(self):
        pass

    def decision(self,check,bet,call,raiseBet,minBet = None):
        if check and bet :
            dec = (input("Check ,Bet or Fold?").lower()).split()
            if dec[0] == 'check':
                self.check()
            elif dec[0] == 'bet':
                self.makeBet(int(dec[1]))
            elif dec[0] =='fold':
                self.fold()
        elif call and raiseBet and minBet != None:
            if minBet > self.moneyBalance:
                dec = input("Call All-in  Or FOLD").lower()
                if dec == 'call':
                    self.call(self.moneyBalance)
                elif dec == 'fold':
                    self.fold()
            else:
                dec = (input("CALL or RAISE ? ").lower()).split()
                if dec[0] == 'call':
                    self.call(minBet)
                elif dec[0] == 'raise':
                    self.makeBet(dec[1])


