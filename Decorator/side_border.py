from border import Border


class SideBorder(Border):

    def __init__(self, display, ch):
        self.display = display
        self.__border_char = ch

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return self.display.get_rows()

    def get_row_text(self, row):
        return self.__border_char + \
            self.display.get_row_text(row) + \
            self.__border_char
