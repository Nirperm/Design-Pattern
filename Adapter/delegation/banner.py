class Banner():

    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print('({0})'.format(self.__string))

    def show_with_aster(self):
        print('*{0}*'.format(self.__string))
