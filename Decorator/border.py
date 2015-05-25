from abc import ABCMeta
from display import Display


class Border(Display, metaclass=ABCMeta):

    # protected Display display
    def _border(self, display):
        self._display = display
