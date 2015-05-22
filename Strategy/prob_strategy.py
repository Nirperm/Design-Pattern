import random
from hand import Hand
from strategy import Strategy


class ProbStrategy(Strategy):

    def __init__(self, seed):
        self.__rand = random.randint(1, seed)
        self.__prev_hand_value = 0
        self.__current_hand_value = 0
        self.__history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def next_hand(self):
        bet = self.__rand(self.__get_sum(self.__current_hand_value))
        hand_value = 0
        if bet < self.__history[self.__current_hand_value][0]:
            hand_value = 0
        elif bet < self.__history[self.__current_hand_value][0] + \
                self._history[self.__current_hand_value][1]:
            hand_value = 1
        else:
            hand_value = 2

        self.__prev_hand_value = self.__current_hand_value
        self.__current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def __get_sum(self, hv):
        total = 0
        for i in range(1, 3):
            total += self.__history[hv][i]
        return total

    def study(self, win):
        if win:
            self.__history[self.__prev_hand_value][self.__current_handvalue] \
                += 1
        else:
            self.__history[self.__prev_hand_value][(self.__current_handvalue + 1) % 3] \
                += 1
            self.__history[self.__prev_hand_value][(self.__current_handvalue + 2) % 3] \
                += 1
