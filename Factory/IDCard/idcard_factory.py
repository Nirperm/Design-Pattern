from Framework.factory import Factory
from IDCard.idcard import IDCard


class IDCardFactory(Factory):

    def __init__(self):
        self.__registed = []

    def _createproduct(self, owner):
        return IDCard(owner)

    def _registerproduct(self, product):
        self.__registed.append(product.getowner())
