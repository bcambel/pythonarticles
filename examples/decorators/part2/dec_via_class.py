import logging
import random
from datetime import datetime as dt
import time

logging.basicConfig(format='[%(asctime)s](%(filename)s#%(lineno)d)%(levelname)-7s %(message)s',
                    level=logging.NOTSET)

class intercept_me(object):
   def __init__ (self, func):
      self.func = func
      logging.debug(id(self))

   def __call__ (self, *args, **kwargs):
      return self.func (*args, **kwargs)

@intercept_me
def some_slow_function():
    logging.info("Will sleep a bit..")
    time.sleep(1+ int((random.random()*10)%5))
    return 'boohoo'

for i in range(0,2):
    logging.info("{0} Starting iter {1}{0}".format(20*"=",i+1))
    logging.info(some_slow_function())

logging.info("done")