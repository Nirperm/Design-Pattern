# from printable import Printable
from printer_proxy import PrinterProxy


if __name__ == "__main__":
    pp = PrinterProxy('Alice')
    print('名前は現在' + pp.get_printer_name() + 'です。')
    pp.set_printer_name('Bob')
    print('名前は現在' + pp.get_printer_name() + 'です。')
    pp.my_print('Hello, world.')
