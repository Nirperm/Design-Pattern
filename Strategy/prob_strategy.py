import random
from hand import Hand
from strategy import Strategy


class ProbStrategy(Strategy):
    def __init__(self):
        self._rand = random.randint(1, 3)
        self._prev_hand_value = 0
        self._current_hand_value = 0
        self._history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def next_hand(self):
        bet = self._rand(self._get_sum(self._current_hand_value))
        hand_value = 0
        if bet < self._history[self._current_hand_value][0]:
            hand_value = 0
        elif bet < self._history[self._current_hand_value][0] + \
                self._history[self._current_hand_value][1]:
            hand_value = 1
        else:
            hand_value = 2

        self._prev_hand_value = self._current_hand_value
        self._current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def __get_sum(self, hv):
        total = 0
        for i in range(1, 3):
            total += self._history[hv][i]
        return total

    def study(self, win):
        if win:
            self._history[self._prev_hand_value][self._current_handvalue] \
                += 1
        else:
            self._history[self._prev_hand_value][(self._current_handvalue + 1) % 3] \
                += 1
            self._history[self._prev_hand_value][(self._current_handvalue + 2) % 3] \
                += 1
