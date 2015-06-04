from abc import ABCMeta, abstractmethod
from element import Element


class Entry(Element):
    __meta__ = ABCMeta

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry):
        raise OSError

    def iterator(self):
        raise OSError

    def to_string(self):
        return self.get_name() + '(' + str(self.get_size()) + ')'
