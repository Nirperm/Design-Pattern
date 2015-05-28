import random
from number_generator import NumberGenerator


class RandomNumberGenerator(NumberGenerator):

    def __init__(self):
        self.__random = random  # FIXME number is random
        self.__number = random.randint(0, 50)  # FIXME 現在の数

    def get_number(self):
        return self.__number

    def execute(self):
        for i in range(0, 20):
            self.__number = self.__random.randint(0, 50)
            self.notify_observers()
