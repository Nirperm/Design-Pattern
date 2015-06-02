import random
from number_generator import NumberGenerator


class RandomNumberGenerator(NumberGenerator):

    __number = 0

    def __init__(self):
        self.__rand = random

    def get_number(self):
        return self.__number

    def execute(self):
        for i in range(0, 20):
            self.__number = self.__rand.randint(0, 50)
            self.notify_observers()
