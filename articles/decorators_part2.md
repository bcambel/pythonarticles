In the part 1, we described the most basic usage of the decorators. Decorators are functions that intercepts the actual implementation
and do something. Remember that functions are first class citizens(objects) in Python.

Fire up your favorite terminal, navigate to code directory and initialize python; start typing 

```python
>>> from ver2 import *
>>> original_int = int
>>> @intercept_me
... def int(value):
...     logging.info("Overwritten integer function is here :)")
...     res = original_int( value )
...     return res
... 
>>> int(10000)
[2013-07-09 20:11:09,906](ver2.py#20)DEBUG   Starting capturing the time of the executing 'int'
[2013-07-09 20:11:09,906](<stdin>#3)INFO    Overwritten integer function is here :)
[2013-07-09 20:11:09,907](ver2.py#25)DEBUG   Function: [int] => Took [0:00:00.000226]
10000
>>> int("231232")
[2013-07-09 20:11:15,875](ver2.py#20)DEBUG   Starting capturing the time of the executing 'int'
[2013-07-09 20:11:15,876](<stdin>#3)INFO    Overwritten integer function is here :)
[2013-07-09 20:11:15,876](ver2.py#25)DEBUG   Function: [int] => Took [0:00:00.000315]
231232
>>> 

```

Python builtin function **int** overriden at the above code, and we redefined the int function. Now, whenever you call
the int function, our decorator will take presedance and calculate the performance of the integer. Be aware that
this is not a good way to time execution of a program or function, but think of it is as a informant.

Implement decorator via a class
-------------------------------

```python
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
```

will result in the following output in your console. As you see, the constructor of our class is only called one time,
which means that the class is initialized only one time.

```
[2013-07-09 21:05:07,815](dec_via_class.py#12)DEBUG   4300575376
[2013-07-09 21:05:07,815](dec_via_class.py#24)INFO    ==================== Starting iter 1====================
[2013-07-09 21:05:07,815](dec_via_class.py#19)INFO    Will sleep a bit..
[2013-07-09 21:05:10,816](dec_via_class.py#25)INFO    boohoo
[2013-07-09 21:05:10,816](dec_via_class.py#24)INFO    ==================== Starting iter 2====================
[2013-07-09 21:05:10,816](dec_via_class.py#19)INFO    Will sleep a bit..
[2013-07-09 21:05:13,817](dec_via_class.py#25)INFO    boohoo
[2013-07-09 21:05:13,817](dec_via_class.py#27)INFO    done
```


