from abc import ABCMeta, abstractmethod


class Element(ABCMeta):

    @abstractmethod
    def accept(self, visitor):
        pass
