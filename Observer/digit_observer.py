import time
import logging
from observer import Observer


class DigitObserver(Observer):

    def update(self, generator):
        print('DigitObserver:' + str(generator.get_number()))
        try:
            time.sleep(1)
        except InterruptedError as e:
            logging.exception(e)
