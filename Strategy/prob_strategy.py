import random
from hand import Hand
from strategy import Strategy


class ProbStrategy(Strategy):
    def __init__(self):
        self.rand = random.randint(1, 3)
        self.prev_hand_value = 0
        self.current_hand_value = 0
        self.history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def next_hand(self):
        bet = self.rand(self.__get_sum(self.current_hand_value))
        hand_value = 0
        if bet < self.history[self.current_hand_value][0]:
            hand_value = 0
        elif bet < self.history[self.current_hand_value][0] + self.history[self.current_hand_value][1]:
            hand_value = 1
        else:
            hand_value = 2

        self.prev_hand_value = self.current_hand_value
        self.current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def __get_sum(self, hv):
        total = 0
        for i in range(1, 3):
            total += self.history[hv][i]
        return total

    def study(self, win):
        if win:
            self.history[self.prev_hand_value][self.current_handvalue] += 1
        else:
            self.history[self.prev_hand_value][(self.current_handvalue + 1) % 3] += 1
            self.history[self.prev_hand_value][(self.current_handvalue + 2) % 3] += 1
