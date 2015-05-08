import sys
from abstract_display import AbstractDisplay


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def opening(self):
        self.print_line()

    def printing(self):
        print('|' + self.string + '|')

    def closing(self):
        self.print_line()

    def print_line(self):
        sys.stdout.write("".join(("+", "-" * self.width, "+\n")))  # printを使うと出力直後に空白が一文字出てしまう
