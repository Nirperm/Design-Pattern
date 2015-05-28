from abc import ABCMeta, abstractmethod


class Observer(Exception):
    __meta__ = ABCMeta

    @abstractmethod
    def update(self, generator):
        pass
