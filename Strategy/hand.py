class Hand():
    HANDVALUE_ROCK = 0
    HANDVALUE_SCISSORS = 1
    HANDVALUE_PAPER = 2

    def __init__(self, handvalue):
        self.__NAMES = ['グー', 'チョキ', 'パー']
        self.__handvalue = handvalue
        self.__hand = [self.HANDVALUE_ROCK,
                       self.HANDVALUE_SCISSORS,
                       self.HANDVALUE_PAPER]

    def get_hand(self, handvalue):
        return self.__hand[self.__handvalue]

    def is_stronger_than(self, h):
        return self.__fight(h) == 1

    def is_weaker_than(self, h):
        return self.__fight(h) == -1

    def __fight(self, h):
        if self == h:
            return 0
        elif (self.__handvalue + 1) % 3 == self.__handvalue:
            return 1
        else:
            return -1

    def to_string(self):
        return self.__NAMES[self.__handvalue]
