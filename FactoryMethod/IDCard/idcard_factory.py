from Framework.factory import Factory
from IDCard.idcard import IDCard


class IDCardFactory(Factory):

    def __init__(self):
        self.__registed = []

    def _create_product(self, owner):
        return IDCard(owner)

    def _register_product(self, product):
        self.__registed.append(product.get_owner())
