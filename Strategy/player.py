class Player():

    __wincount = 0
    __losecount = 0
    __gamecount = 0

    def __init__(self, name, strategy):
        self.__name = name
        self.__strategy = strategy

    def next_hand(self):
        return self.__strategy.next_hand()

    def win(self):
        self.__strategy.study(True)
        self.__wincount += 1
        self.__gamecount += 1

    def lose(self):
        self.__strategy.study(False)
        self.__losecount += 1
        self.__gamecount += 1

    def even(self):
        self.__gamecount += 1

    def to_stirng(self):
        return '[{0}: {1} games {2} win {3} lose]'.format(self.__name,
                                                          self.__gamecount,
                                                          self.__wincount,
                                                          self.__losecount)
