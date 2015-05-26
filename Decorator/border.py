from abc import ABCMeta
from display import Display


class Border(Display):

    __metaclass__ = ABCMeta

    def _border(self, display):
        self._display = display
