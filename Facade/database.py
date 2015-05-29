import configparser
import logging
import sys


class Database():

    def get_properties(self, dbname):
        filename = sys.argv[1]
        self.filename = dbname + '.txt'
        self.prop = configparser.ConfigParser()
        try:
            self.prop.read(filename)
        except IOError:
            logging.exception('Warning' + filename + 'is not found.')
        return self.prop
