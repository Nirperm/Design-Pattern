from abc import ABCMeta, abstractmethod
from file_treatment_exception import FileTreatmentException


class Entry():  # mataclass=ABCMeta

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def print_list(self):
        self._print_list('')
        # protected abstract void printList(String prefix) FIXME change scope asccess?

    def _printe_list(self):
        pass

    def add(self):
        FileTreatmentException.except_file_treatment()  # FIXME ??

    def to_string(self):
        return self.get_name() + '(' + self.get_size() + ')'
