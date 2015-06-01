class Hand():
    HANDVALUE_ROCK = 0
    HANDVALUE_SCISSORS = 1
    HANDVALUE_PAPER = 2
    NAMES = ['グー', 'チョキ', 'パー']
    HANDS = [HANDVALUE_ROCK,
             HANDVALUE_SCISSORS,
             HANDVALUE_PAPER]

    def __init__(self, handvalue):
        self.__handvalue = handvalue

    def get_hand(self, handvalue):
        return self.HANDS[self.__handvalue]

    def is_stronger_than(self, h):
        return self.__fight(h) == 1

    def is_weaker_than(self, h):
        return self.__fight(h) == -1

    def __fight(self, h):
        if self.__handvalue == h.__handvalue:
            return 0
        elif (self.__handvalue + 1) % 3 == h.__handvalue:
            return 1
        else:
            return -1

    def to_string(self):
        return self.NAMES[self.__handvalue]
