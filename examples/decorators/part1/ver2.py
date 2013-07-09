import time
import logging
import random 
from datetime import datetime as dt
from functools import wraps

logging.basicConfig(format='[%(asctime)s](%(filename)s#%(lineno)d)%(levelname)-7s %(message)s',
                    level=logging.NOTSET)


def intercept_me(intercepted_function_reference):
    
    @wraps(intercepted_function_reference)
    def timer(*args, **kwargs):
        '''*args and **kwargs are the parameters that are supplied to our original function'''
        # get our actual function name
        function_name = intercepted_function_reference.func_name
        # call our actual function
        # store the return of the function in a parameter
        logging.debug("Starting capturing the time of the executing '%s'" % function_name)
        start = dt.now()
        actual_result = intercepted_function_reference(*args, **kwargs)
        stop = dt.now()
        execution_time = stop - start
        logging.debug('Function: [{fnc}] => Took [{timed}]'.format(fnc=function_name, timed=execution_time))
        
        return actual_result
    # return our inner function which will intercept the call
    return timer

@intercept_me
def some_slow_function():
    logging.info("Will sleep a bit..")
    time.sleep(1+ int((random.random()*10)%5))
    return 'boohoo'

for i in range(0,10):
    logging.info("{0} Starting iter {1}{0}".format(20*"=",i+1))
    logging.info(some_slow_function())
    

# [2013-07-09 14:40:38,451](ver2.py#37)INFO    ==================== Starting iter 1====================
# [2013-07-09 14:40:38,451](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:38,451](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:40:41,452](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:03.001206]
# [2013-07-09 14:40:41,452](ver2.py#38)INFO    boohoo
# [2013-07-09 14:40:41,452](ver2.py#37)INFO    ==================== Starting iter 2====================
# [2013-07-09 14:40:41,453](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:41,453](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:40:43,453](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:02.000476]
# [2013-07-09 14:40:43,453](ver2.py#38)INFO    boohoo
# [2013-07-09 14:40:43,454](ver2.py#37)INFO    ==================== Starting iter 3====================
# [2013-07-09 14:40:43,454](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:43,454](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:40:46,455](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:03.001121]
# [2013-07-09 14:40:46,455](ver2.py#38)INFO    boohoo
# [2013-07-09 14:40:46,455](ver2.py#37)INFO    ==================== Starting iter 4====================
# [2013-07-09 14:40:46,455](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:46,456](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:40:48,456](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:02.000194]
# [2013-07-09 14:40:48,456](ver2.py#38)INFO    boohoo
# [2013-07-09 14:40:48,456](ver2.py#37)INFO    ==================== Starting iter 5====================
# [2013-07-09 14:40:48,456](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:48,457](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:40:50,458](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:02.001092]
# [2013-07-09 14:40:50,458](ver2.py#38)INFO    boohoo
# [2013-07-09 14:40:50,458](ver2.py#37)INFO    ==================== Starting iter 6====================
# [2013-07-09 14:40:50,458](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:50,458](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:40:54,459](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:04.001043]
# [2013-07-09 14:40:54,460](ver2.py#38)INFO    boohoo
# [2013-07-09 14:40:54,460](ver2.py#37)INFO    ==================== Starting iter 7====================
# [2013-07-09 14:40:54,460](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:54,460](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:40:56,461](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:02.001127]
# [2013-07-09 14:40:56,461](ver2.py#38)INFO    boohoo
# [2013-07-09 14:40:56,462](ver2.py#37)INFO    ==================== Starting iter 8====================
# [2013-07-09 14:40:56,462](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:40:56,462](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:41:01,463](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:05.001058]
# [2013-07-09 14:41:01,463](ver2.py#38)INFO    boohoo
# [2013-07-09 14:41:01,463](ver2.py#37)INFO    ==================== Starting iter 9====================
# [2013-07-09 14:41:01,463](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:41:01,464](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:41:05,465](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:04.001060]
# [2013-07-09 14:41:05,465](ver2.py#38)INFO    boohoo
# [2013-07-09 14:41:05,465](ver2.py#37)INFO    ==================== Starting iter 10====================
# [2013-07-09 14:41:05,465](ver2.py#19)DEBUG   Starting capturing the time of the executing 'some_slow_function'
# [2013-07-09 14:41:05,465](ver2.py#32)INFO    Will sleep a bit..
# [2013-07-09 14:41:09,466](ver2.py#24)DEBUG   Function: [some_slow_function] => Took [0:00:04.001083]
# [2013-07-09 14:41:09,467](ver2.py#38)INFO    boohoo
