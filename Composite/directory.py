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
            size += super(Directory, d_name).get_size()
        return size

    def add(self, entry):
        self.__directory.append(entry)  # FIXME java list add?
        # http://qiita.com/sukoyakarizumu/items/490402b6fa52cb7c4023
        return self

    def _print_list(self, prefix):
        # print(prefix + '/' + self)  # FIXME ??
        for d_name in self.__directory:
            super(Directory, d_name).print_list(prefix + '/' + self.__name)
