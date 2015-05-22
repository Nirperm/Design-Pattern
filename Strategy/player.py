from strategy import Strategy


class Player():

    def __init__(self, name, strategy):
        self.__name = name
        self.__strategy = Strategy
        self.__wincount = 0
        self.__losecount = 0
        self.__gamecount = 0

    def next_hand(self):
        return self.__strategy.next_hand()

    def win(self):
        self.__strategy.study(True)
        self.__wincount += 1
        self.__gamecount += 1

    def lose(self):
        self.__strategy.study(False)
        self.__wincount += 1
        self.__losecount += 1

    def even(self):
        self.__gamecount += 1

    def to_stirng(self):
        return '([{0}: {1} games \
                 {2} win {3} lose])'.format(self.__name,
                                            self.__gamecount,
                                            self.__wincount,
                                            self.__losecount)
