import time
import logging
from observer import Observer


class DigitObserver(Observer):  # FIXME: doule inheritance

    def update(self, generator):
        print('DigitObserver:' + generator.get_number())
        try:
            time.sleep(1)
        except InterruptedError as e:
            logging.exception(e)
