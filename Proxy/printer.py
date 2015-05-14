import sys
import time
from printable import Printable


class Printer(Printable):   # 名前つきのプリンタを表すクラス(本人)

    def __init__(self, name):
        self.name = name
        # self.__heavy_job('Printerのインスタンス生成中')
        self.__heavy_job('Printerのインスタンス{0}を生成中'.format(self.name))

    def set_printer_name(self, name):
        self.name = name

    def get_printer_name(self):
        return self.name

    def my_print(self, string):
        print('===' + self.name + '===')
        print(string)

    def __heavy_job(self, msg):
        print(msg)
        for i in range(1, 5):
            try:
                time.sleep(1)
            except InterruptedError:
                sys.stdout.write('.')
        sys.stdout.write('完了')
