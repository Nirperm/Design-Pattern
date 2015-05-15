from file_treatment_exception import FileTreatmentException


class Entry():

    def get_name(self):
        pass

    def get_size(self):
        pass

    def print_list(self):
        self.print_list('')
        # protected abstract void printList(String prefix) FIXME change scope access?

    def add(self):
        FileTreatmentException.except_file_treatment()  # FIXME ??

    def to_string(self):
        return self.get_name() + '(' + self.get_size() + ')'
