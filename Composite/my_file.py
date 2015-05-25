from entry import Entry


class MyFile(Entry):

    def __init__(self, name, string):
        self.__name = name
        self.__string = string

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def _print_list(self, prefix):
        print(prefix + '/' + Entry.to_string())
