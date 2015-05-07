# from abc import ABCMeta
from abc import *


class Printer():
    __metalcass__ = ABCMeta

    def __init__(self, string):
        self.string = string

    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass
