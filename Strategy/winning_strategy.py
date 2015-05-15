import random
from hand import Hand
from strategy import Strategy


class WinningStrategy(Strategy):

    def __init__(self):
        self._rand = random.randint(1, 3)
        self._won = False

    def next_hand(self):
        if not(self._won):
            prev_hand = Hand.get_hand(self._rand)
        return prev_hand

    def study(self, win):
        self._won = win
