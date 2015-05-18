from display import Display


class StringDisplay(Display):
    """ 一行の文字列を表示するクラス
        Displayクラスのサブクラスなので、
        Displayクラスで宣言されている
        抽象メソッドを実装する責務がある """

    def __init__(self, string):
        """ 引数で表示文字列を指定 """
        self._string = string

    def get_columns(self):
        """ 文字数 """
        return len(self._string)

    def get_rows(self):
        """ 行数は1 """
        return 1

    def get_row_text(self, row):
        """ rowが0の時のみ返す """
        if row == 0:
            return self._string
        else:
            return False
