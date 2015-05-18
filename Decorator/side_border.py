from border import Border
from display import Display


class SideBorder(Border):
    # FIXME displayはinit時はDisplayクラス, get_rows時はStringDisplayを使いたい
    """ 具体的な飾り枠の一種のBorderクラスのサブクラス """

    def __init__(self, display, ch):
        """ コンストラクタでDisplayと飾り文字を指定 """
        super(self.display)
        self._border_char = ch

    def get_columns(self, display):
        """ 文字数は中身の両側に飾り文字分を加えたもの """
        return 1 + display.get_columns() + 1

    def get_rows(self):
        """ 行数は中身の行数に同じ """
        return self.display.get_rows()

    def get_row_text(self, display, row):
        """ 指定行の内容は、中身の指定行の両側に飾り文字を付けたもの """
        return self._border_char + display.get_row_text(row) + self._border_char
