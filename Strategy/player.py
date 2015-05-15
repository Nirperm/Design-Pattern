from strategy import Strategy


class Player():

    def __init__(self, name, Strategy):
        self._name = name
        self._strategy = Strategy
        self._wincount = 0
        self._losecount = 0
        self._gamecount = 0

    def next_hand(self):
        return self.strategy.next_hand()

    def win(self):
        self._strategy.study(True)
        self._wincount += 1
        self._gamecount += 1

    def lose(self):
        self._strategy.study(False)
        self._wincount += 1
        self._losecount += 1

    def even(self):
        self._gamecount += 1

    def to_stirng(self):
        return '([{0}: {1} games \
                 {2} win {3} lose])'.format(self._name,
                                            self._gamecount,
                                            self._wincount,
                                            self._losecount)
