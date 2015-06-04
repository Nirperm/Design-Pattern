from entry import Entry


class MyFile(Entry):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def accept(self, visitor):
        visitor.visit(self)
