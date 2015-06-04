from entry import Entry


class Directory(Entry):

    __dir = []

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_size(self):
        size = 0
        for d in self.__dir:
            size += d.get_size()
        return size

    def add(self, entry):
        self.__dir.add(entry)
        return self

    def iterator(self):
        return self.__dir.iterator()

    def accept(self, v):
        v.visit(self)
