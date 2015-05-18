from display import Display


class Border(Display):
    """ 飾り枠を表す抽象クラス """

    # protected Display display
    def _border(self, display):
        """ インスタンス生成時に「中身」を引数で指定 """
        self._display = display
