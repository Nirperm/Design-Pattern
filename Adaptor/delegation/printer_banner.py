from printer import Printer
from banner import Banner


class PrinterBanner(Printer):
    def __init__(self, string):
        self.banner = Banner(string)

    def print_weak(self):
        self.banner.show_with_paren()

    def print_strong(self):
        self.banner.show_with_aster()
