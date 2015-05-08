import sys
from abstract_display import AbstractDisplay


class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def opening(self):
        sys.stdout.write('<<')  # printを使うと出力直後に空白が一文字出てしまう

    def printing(self):
        sys.stdout.write(self.ch)

    def closing(self):
        print('>>')
