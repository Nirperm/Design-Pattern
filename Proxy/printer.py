import sys
import time
from printable import Printable


class Printer(Printable):   # 名前つきのプリンタを表すクラス(本人)

    def __init__(self, name):
        self.__heavy_job('Printerのインスタンス生成中')

    def set_printer_name(self, name):
        self.__name = name
        self.__heavy_job('Printerのインスタンス{0}を生成中'.format(self.__name))

    def get_printer_name(self):
        return self.__name

    def my_print(self, string):
        print('===' + self.__name + '===')
        print(string)

    def __heavy_job(self, msg):
        print(msg)
        for i in range(1, 5):
            try:
                time.sleep(1)
            except InterruptedError:
                sys.stdout.write('.')
        sys.stdout.write('完了')
