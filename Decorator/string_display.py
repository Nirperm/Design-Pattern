from display import Display


class StringDisplay(Display):

    def __init__(self, string):
        self.__string = string

    def get_columns(self):
        return len(self.__string)

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        if row == 0:
            return self.__string
        else:
            return False
