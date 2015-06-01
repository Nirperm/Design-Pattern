import random
from hand import Hand
from strategy import Strategy


class ProbStrategy(Strategy):

    __prev_hand_value = 0
    __current_hand_value = 0
    __history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def __init__(self, seed):
        self.__rand = seed

    def next_hand(self):
        bet = random.randint(0, self.__get_sum(self.__current_hand_value))  # TODO find best solution
        hand_value = 0
        if bet < self.__history[self.__current_hand_value][0]:
            hand_value = 0
        elif bet < self.__history[self.__current_hand_value][0] + \
                self.__history[self.__current_hand_value][1]:
            hand_value = 1
        else:
            hand_value = 2

        self.__prev_hand_value = self.__current_hand_value
        self.__current_hand_value = hand_value

        return Hand(bet).get_hand(hand_value)  # TODO find best solution

    def __get_sum(self, hv):
        total = 0
        for i in range(0, 3):
            total += self.__history[hv][i]
        total = 2 if total > 2 else total  # TODO find best solution
        return total

    def study(self, win):
        if win:
            self.__history[self.__prev_hand_value][self.__current_hand_value] \
                += 1
        else:
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 1) % 3] \
                += 1
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 2) % 3] \
                += 1
