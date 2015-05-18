class Display():
    """ 複数行からなる文字列表示の抽象クラス
        get_columns, get_rows, get_row_textはサブクラスで実装 """

    def get_columns(self):
        """ 横の文字数を得る """
        pass

    def get_rows(self):
        """ 縦の行数を得る """
        pass

    def get_row_text(self):
        """ row番目の文字列を得る """
        pass

    def show(self):
        """ 全表示する """
        for i in range(self.get_rows()):
            print(self.get_row_text(i))
