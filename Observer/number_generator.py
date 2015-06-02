from abc import ABCMeta, abstractmethod


class NumberGenerator(metaclass=ABCMeta):

    __observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)

    @abstractmethod
    def get_number():
        pass

    @abstractmethod
    def execute():
        pass
