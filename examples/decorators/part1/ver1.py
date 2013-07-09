import time
import logging
import random 

logging.basicConfig(format='[%(asctime)s](%(filename)s#%(lineno)d)%(levelname)-7s %(message)s',
                    level=logging.NOTSET)


def intercept_me(intercepted_function_reference):
    # *args and **kwargs are the parameters that are supplied to our original function
    def timer(*args, **kwargs):
        # call our actual function
        # store the return of the function in a parameter
        logging.debug("==I'm the timer within the decorator=intercept_me")
        actual_result = intercepted_function_reference(*args, **kwargs)
        logging.debug("Completed function call. Result => %s" % actual_result)
        return actual_result
    # return our inner function which will intercept the call
    return timer

@intercept_me
def some_slow_function():
    logging.info("Will sleep a bit..")
    time.sleep(1+ int((random.random()*10)%5))
    return 'boohoo'

logging.info(some_slow_function())
logging.info("Done....")

#[2013-07-09 14:46:39,311](test.py#14)DEBUG   ==I'm the timer within the decorator=intercept_me
#[2013-07-09 14:46:39,311](test.py#23)INFO    Will sleep a bit..
#[2013-07-09 14:46:40,312](test.py#16)DEBUG   Completed function call. Result => boohoo
#[2013-07-09 14:46:40,312](test.py#27)INFO    boohoo
#[2013-07-09 14:46:40,312](test.py#28)INFO    Done....
