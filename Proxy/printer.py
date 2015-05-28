import sys
import time
from printable import Printable


class Printer(Printable):

    def __init__(self, name):
        self.__name = name
        self.__heavy_job('Printerのインスタンス({0})を生成中'.format(self.__name))

    def set_printer_name(self, name):
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def my_print(self, string):
        print('===' + ' ' + self.__name + ' ' + '===')
        print(string)

    def __heavy_job(self, msg):
        sys.stdout.write(msg)
        for i in range(1, 5):
            try:
                time.sleep(1)  # TODO  Thread.sleep
            except InterruptedError:
                pass
            sys.stdout.write('.')
        print('完了。')
