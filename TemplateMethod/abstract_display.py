class AbstractDisplay():

    def opening(self):
        pass

    def printing(self):
        pass

    def closing(self):
        pass

    def display(self):
        self.opening()
        for i in range(5):
            self.printing()
        self.closing()
