from abc import ABCMeta, abstractmethod
from functools import singledispatch


class Visitor():  # mataclass=ABCMeta):

    # TODO: use singledispatch
    @abstractmethod
    def visit(self, file_or_directory):
        pass
