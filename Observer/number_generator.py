from abc import ABCMeta, abstractmethod


class NumberGenerator(metaclass=ABCMeta):

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        """ this is java
        Iterator it = observers.iterator();
        while (it.hasNext()){
            Observer o = (Observer)it.next();
            o.update(this)
        }
        """
        pass

    @abstractmethod
    def get_number():
        pass

    @abstractmethod
    def execute():
        pass
