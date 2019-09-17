class Card:

    def __init__(self,value,suit):
        self.__value = value
        self.__suit = suit
        self.__code = self.decode(self.__value)

    def getCode(self):
        return self.__code

    def decode(self,value):
        if value == 'T':
            return 10
        elif value == 'J':
           return 11
        elif value == 'Q':
            return 12
        elif value == 'K':
            return 13
        elif value == 'A':
            return 14
        else:
            return int(value)

    def __repr__(self):
        return self.__value + self.__suit

    def __str__(self):
        return self.__value + self.__suit