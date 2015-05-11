from Framework import product as Product


class IDCard(Product):
    def __init__(self, owner):
        self.__owner = owner
        print(owner + 'のカードを作ります。')

    def use(self):
        print(self.__owner + 'のカードを使います。')

    def get_owner(self):
        return self.__owner
