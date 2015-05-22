from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def next_hand():
        pass

    @abstractmethod
    def study(win):
        pass
