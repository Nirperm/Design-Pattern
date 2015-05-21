from abc import ABCMeta, abstractmethod

class AbstractDisplay(metaclass=ABCMeta):

    @abstractmethod
    def opening(self):
        pass

    @abstractmethod
    def printing(self):
        pass

    @abstractmethod
    def closing(self):
        pass

    def display(self):
        self.opening()
        for i in range(5):
            self.printing()
        self.closing()
