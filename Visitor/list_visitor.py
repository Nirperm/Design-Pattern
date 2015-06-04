from visitor import Visitor
from functools import singledispatch


class ListVisitor(Visitor):

    __currentdir = ''

    # TODO: use singledispatch
    def visit(self, my_file):
        print(self.__currentdir + '/' + my_file)

    def visit(self, directory):
        print(self.__currentdir + '/' + directory)
        savedir = self.__currentdir
        self.__currentdir = self.__currentdir + '/' + directory.get_name()
        for d in directory:
            d.accept(self)

        self.__currentdir = savedir
