from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def _createproduct(self, owner):
        pass

    @abstractmethod
    def _registerproduct(self, product):
        pass

    def create(self, owner):
        self.__p = self._createproduct(owner)
        self._registerproduct(self.__p)
        return self.__p
