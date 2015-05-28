import time
from observer import Observer


class GraphObserver(Observer):  # FIXME: doule inheritance

    def update(self, generator):
        print('GraphObserver:')
        count = generator.get_number()
        for i in range(0, count):
            print('*')
        print('')
        try:
            time.sleep(10)
        except InterruptedError:
            pass
