from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):

    @abstractmethod
    def _create_product(self, owner):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass

    def create(self, owner):
        self.__p = self._create_product(owner)
        self._register_product(self.__p)
        return self.__p
