from entry import Entry


class MyFile(Entry):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def _print_list(self, prefix):
        print(prefix + '/' + self.to_string())
