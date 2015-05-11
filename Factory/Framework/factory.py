class Factory():
    def _create_product(self, owner):
        pass

    def _register_product(self, product):
        pass

    def create(self, owner):
        # オーバライドさせない、つまり外部から参照できなくさせる
        self.__product = self._create_product(owner)
        self._register_product(self.__product)
        return self.__product
