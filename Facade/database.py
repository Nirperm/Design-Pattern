from configparser import ConfigParser
import logging


class Database():

    def get_properties(self, dbname):
        filename = dbname + '.ini'
        conf = ConfigParser()
        try:
            conf.read(filename)
            user_name = conf['TEST1']['hyuki@hyuki.com']
            return user_name
        except IOError:
            logging.exception('Warning' + filename + 'is not found.')
