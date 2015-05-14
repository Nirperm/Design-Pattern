import random
from hand import Hand
from strategy import Strategy


class WinningStrategy(Strategy):
    def __init__(self):
        self.__rand = random.randint(1, 3)
        self.__won = False

    def next_hand(self):
        if not(self.__won):
            prev_hand = Hand.get_hand(self.__rand)
        return prev_hand

    def study(self, win):
        self.__won = win
