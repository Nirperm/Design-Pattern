from builder import Builder


class TextBuilder(Builder):
    __buffer = []

    def make_title(self, title):
        self.__buffer.append('=' * 20)
        self.__buffer.append('[' + title + ' ]\n')
        self.__buffer.append('\n')

    def make_string(self, string):
        self.__buffer.append('■' + string + '\n')
        self.__buffer.append('\n')

    def make_items(self, items):
        for i in range(0, len(items)):
            self.__buffer.append(' ' + items[i] + '\n')
        self.__buffer.append('\n')

    def close(self):
        self.__buffer.append('=' * 20)

    def get_result(self):
        return self.__buffer  # to_string
