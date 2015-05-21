import sys
from abstract_display import AbstractDisplay


class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.__ch = ch

    def opening(self):
        sys.stdout.write('<<')

    def printing(self):
        sys.stdout.write(self.__ch)

    def closing(self):
        print('>>')
