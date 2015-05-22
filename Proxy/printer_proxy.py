from printable import Printable
from printer import Printer


class PrinterProxy(Printable):

    def __init__(self, name):
        self.__name = name
        self.__real = Printer(self.__name)  # FIXME 本来はここではしないはず

    def set_printer_name(self, name):
        if not(self.__real is None):
            self.__real.set_printer_name(name)
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def my_print(self, string):
        self.__realize()
        self.__real.my_print(string)

    def __realize(self):
        if (self.__real is None):
            self.__real = Printer(self.__name)
