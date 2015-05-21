import sys
from abstract_display import AbstractDisplay


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.__string = string
        self.__width = len(string)

    def opening(self):
        self.__print_line()

    def printing(self):
        print('|' + self.__string + '|')

    def closing(self):
        self.__print_line()

    def __print_line(self):
        sys.stdout.write(''.join(('+', '-' * self.__width, '+\n')))
