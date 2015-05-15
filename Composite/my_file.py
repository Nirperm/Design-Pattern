from entry import Entry


class MyFile(Entry):

    def __init__(self, name, string):
        self._name = name
        self._string = string

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def _print_list(self, prefix):
        print(prefix + '/' + Entry.to_string())
