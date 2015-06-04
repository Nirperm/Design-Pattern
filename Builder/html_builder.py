import logging
from builder import Builder


class HTMLBuilder(Builder):

    def make_title(self, title):
        self.__filename = title + '.html'

        try:
            self.__writer = open(self.__filename, mode='w')
        except IOError as e:
            logging.exception(e)

        self.__writer.write('<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title>' + title + '</title></head><body>')
        self.__writer.write('<h1>' + title + '<h1>')

    def make_string(self, string):
        self.__writer.write('<h1>' + string + '</p>')

    def make_items(self, items):
        self.__writer.write('<ul>')
        for i in range(0, len(items)):
            self.__writer.write('<li>' + items[i] + '</li>')
        self.__writer.write('</ul>')

    def close(self):
        self.__writer.write('</body></html>')
        self.__writer.close()

    def get_result(self):
        return self.__filename
