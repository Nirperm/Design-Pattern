from border import Border
from display import Display


class FullBorder(Border):

    """ 上下左右に飾り付けするBorderクラスのサブクラス """

    def __init__(self, display):
        super(self.display)

    def get_columns(self):
        """ 文字数は中身の両側に左右の飾り文字分を加えたもの """
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        """ 行数は中身の行数に上下の飾り文字分を加えたもの """
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0:
            """ 枠の上端 """
            return '+' + self._make_line('-', self.display.get_columns()) + '+'
        elif row == self.display.get_rows() + 1:
            """ 枠の下端 """
            return '+' + self._make_line('-', self.display.get_columns()) + '+'
        else:
            return '|' + self.display.get_row_text(row - 1) + '|'

    def _make_line(self, ch, count):
        """ 文字chをcount個分連続させた文字列を作る """
        # buf = StringIO()
        buf = []
        for i in count:
            buf.append(ch)
        return ' '.join(buf)
