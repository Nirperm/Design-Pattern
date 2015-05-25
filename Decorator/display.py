from abc import ABCMeta, abstractmethod


class Display(metaclass=ABCMeta):

    @abstractmethod
    def get_columns(self):
        pass

    @abstractmethod
    def get_rows(self):
        pass

    @abstractmethod
    def get_row_text(self):
        pass

    def show(self):
        for i in range(self.get_rows()):
            print(self.get_row_text(i))
