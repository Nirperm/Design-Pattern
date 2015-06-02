import sys
import time
from observer import Observer


class GraphObserver(Observer):

    def update(self, generator):
        sys.stdout.write('GraphObserver:')
        count = generator.get_number()
        for i in range(0, count):
            sys.stdout.write('*')
        print('')
        try:
            time.sleep(1)
        except InterruptedError:
            pass
