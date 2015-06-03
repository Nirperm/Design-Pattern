from configparser import ConfigParser
import logging


class Database():

    def get_properties(self, dbname):
        filename = dbname + '.ini'
        conf = ConfigParser()
        try:
            conf.read(filename)
            prob = conf['TEST1']
            return prob
        except IOError:
            logging.exception('Warning' + filename + 'is not found.')
