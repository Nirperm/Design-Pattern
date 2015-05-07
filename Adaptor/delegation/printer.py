# FIXME  not delegation i think
# refer to http://qiita.com/ukisoft/items/b7c410b96dde1922a2d0
from abc import *
# from abc import ABCMeta


class Printer():
    __metalcass__ = ABCMeta

    def __init__(self, string):
        self.weak = self.print_weak(string)
        self.strong = self.print_strong(string)

    @classmethod
    @abstractmethod
    def print_weak(cls, string):
        pass

    @classmethod
    @abstractmethod
    def print_strong(cls, string):
        pass
