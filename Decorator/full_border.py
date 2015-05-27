from border import Border


class FullBorder(Border):

    def __init__(self, display):
        self.display = display

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0:
            return '+' + self._make_line('-', self.display.get_columns()) + '+'
        elif row == self.display.get_rows() + 1:
            return '+' + self._make_line('-', self.display.get_columns()) + '+'
        else:
            return '|' + self.display.get_row_text(row - 1) + '|'

    def _make_line(self, ch, count):
        buf = []
        for i in range(0, count):
            buf.append(ch)
        return ' '.join(buf)
