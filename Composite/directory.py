from entry import Entry


class Directory(Entry):
    __directory = []

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_size(self):
        size = 0
        for d_name in self.directory:
            size += super(Directory, self).get_size()
        return size

    def add(self, entry):
        self.__directory.append(entry)
        return self

    def _print_list(self, prefix):
        print(prefix + '/' + self.get_name())
        for d_name in self.__directory:
            print(prefix + '/' + d_name.get_name())
