from Framework.product import Product


class IDCard(Product):

    def __init__(self, owner):
        self.__owner = owner
        print(self.__owner + 'のカードを作成します')

    def use(self):
        print(self.__owner + 'のカードを使います')

    def get_owner(self):
        return self.__owner
