class Hand():
    def __init__(self, handvalue):
        self.HANDVALUE_ROCK = 0
        self.HANDVALUE_SCISSORS = 1
        self.HANDVALUE_PAPER = 2
        self.__names = ['グー', 'チョキ', 'パー']
        self.handvalue = handvalue

    def get_hand(self, handvalue):
        return self[handvalue]

    def is_stronger_than(self, h):
        return self.__fight(h) == 1

    def is_weaker_than(self, h):
        return self.__fight(h) == -1

    def __fight(self, h):
        if self == h:
            return 0
        elif (self.handvalue + 1) % 3 == self.handvalue:
            return 1
        else:
            return -1

    def to_string(self, handvalue):
        return self.__names[handvalue]
