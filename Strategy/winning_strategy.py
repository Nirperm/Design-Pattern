import random
from hand import Hand
from strategy import Strategy


class WinningStrategy(Strategy):

    __won = False
    __prev_hand = 0

    def __init__(self, seed):
        self.__rand = seed

    def next_hand(self):
        if not(self.__won):
            self.__prev_hand = Hand(self.__rand).get_hand(random.randint(0, 3))  # TODO find best solution
        return self.__prev_hand

    def study(self, win):
        self.__won = win
