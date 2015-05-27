import random
from hand import Hand
from strategy import Strategy


class WinningStrategy(Strategy):

    def __init__(self, seed):
        self.__rand = random.randint(1, seed)
        self.__won = False

    def next_hand(self):
        if not(self.__won):
            __prev_hand = Hand(self.__rand).get_hand(self.__rand)  # TODO find best solution
        return __prev_hand

    def study(self, win):
        self.__won = win
