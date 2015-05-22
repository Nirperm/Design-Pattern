from abc import abstractmethod


class Printable():

    @abstractmethod
    def set_printer_name(self, name):
        pass

    @abstractmethod
    def get_printer_name(self):
        pass

    @abstractmethod
    def my_printer(self, string):
        pass
