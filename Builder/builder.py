from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def make_title(self, title):
        pass

    @abstractmethod
    def make_string(self, string):
        pass

    @abstractmethod
    def make_items(self, items):
        pass

    @abstractmethod
    def close(self):
        pass

