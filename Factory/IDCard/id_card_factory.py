from Framework import factory as Factory
from IDCard import idcard as IDCard


class IDCardFactory(Factory):
    def __init__(self):
        self.__register = []

    def _create_product(self, owner):
        return IDCard(owner)

    def _register_product(self, product):
        self.__register.append(product.getowner())
