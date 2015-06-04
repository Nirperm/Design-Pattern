from banner import Banner


class PrinterBanner(Banner):

    def __init__(self, string):
        super().__init__(string)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()
