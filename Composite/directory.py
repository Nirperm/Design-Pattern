from entry import Entry


class Directory(Entry):
    directory = []

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self.name

    def get_size(self):
        size = 0
        for d_name in self.directory:
            size += super(Directory, d_name).get_size()
        return size

    def add(self, entry):
        self.directory.add(entry)
        return self

    def _print_list(self, prefix):
        print(prefix + '/' + self)  # FIXME ??
        for d_name in self.directory:
            super(Directory, d_name).print_list(prefix + '/' + self.name)
