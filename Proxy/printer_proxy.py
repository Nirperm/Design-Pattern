from printable import Printable
from printer import Printer


class PrinterProxy(Printable):  # 名前つきのプリンタを表すクラス(代理人)
    def __init__(self, name):
        self.name = name
        self.real = Printer(self.name)  # FIXME 本来はここではしないはず

    def set_printer_name(self, name):
        if not(self.real is None):
            self.real.set_printer_name(name)
        self.name = name

    def get_printer_name(self):
        return self.name

    def my_print(self, string):
        self.__realize()
        self.real.my_print(string)

    def __realize(self):
        if (self.real is None):
            self.real = Printer(self.name)
