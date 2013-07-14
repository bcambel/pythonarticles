Decorators are really nice way of doing some work without effecting the actual implementation. Its similar to wire tapping but 
with additional functionality. This article is part 1 for describing the basic usage and the execution flow of the 
decorators. In the next part, we will dive into more detail into the decorator magic.

Let's start with a simple example; say you have functions that takes a bit time to complete, and you want to log 
how much time did it take ?

In this example we will use the following function as the starting point

```python
import time

def some_slow_function():
    time.sleep(1+ int(random.random()))
    return 'boohoo'
```
It will sleep between 1 to 2 seconds and return **boohoo**. 

Adding some flavor into the mix with the following code; Let's call our slow function 3 times.

```python
for i in range(0,3):
    print some_slow_function()
```

When we run the above code ;

```
boohoo
boohoo
boohoo
```

We couldn't capture how many seconds did it take to complete the operation. You might argue that we could add logging statements 
into the mix. That's correct, and you probably should do it. 

Lets define our first decorator. 

```python

# **intercepted_function** is a parameter that will be passed
# by Python before the code works.
def intercept_me(intercepted_function):
    # *args and **kwargs are the parameters that are supplied to our original function
    def timer(*args, **kwargs):
        # call our actual function
        # store the return of the function in a parameter
        actual_result = intercepted_function(*args, **kwargs)
        return actual_result
    # return our inner function which will intercept the call
    return timer
    
@intercept_me
def some_slow_function():
    time.sleep(1+ int(random.random()))
    return 'boohoo'

# lets make a call to see the output
print some_slow_function()    

```

As you see ```time_me``` is a function which returns a function which will intercept the call, but not going to do anything. 
Exactly the same.

```
boohoo
```

Let's rewrite our decorator. Focus on the print line. 

```python
def intercept_me(intercepted_function):
    # *args and **kwargs are the parameters that are supplied to our original function
    def timer(*args, **kwargs):
        # call our actual function
        # store the return of the function in a parameter
        print "==I'm the timer within the decorator=intercept_me"
        actual_result = intercepted_function(*args, **kwargs)
        return actual_result
    # return our inner function which will intercept the call
    return timer

```
and when you run the code you will get

```
==I'm the timer within the decorator=intercept_me
boohoo
```

As you see, the print statement within the decorator, was printed before the **boohoo**. 
Let's add more logging statements to see the code flow more clear.

```python
import time
import logging
import random 

logging.basicConfig(format='[%(asctime)s](%(filename)s#%(lineno)d)%(levelname)-7s %(message)s',
                    level=logging.NOTSET)


def intercept_me(intercepted_function):
    # *args and **kwargs are the parameters that are supplied to our original function
    def timer(*args, **kwargs):
        # call our actual function
        # store the return of the function in a parameter
        logging.debug("==I'm the timer within the decorator=intercept_me")
        actual_result = intercepted_function(*args, **kwargs)
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
```

The result of the implementation is as follows. All the decorator related logging statements are DEBUG and the rest is INFO
After **Line#15** the actual call is made which you will get the next (**Line#27**) INFO logging.
**Boohoo** is printed after the DEBUG statement **line#16** because the return of the function call is used within the 
**line#23** <code>logging.info(some_slow_function())</code>

```
[2013-07-09 14:20:08,903](test.py#14)DEBUG   ==I'm the timer within the decorator=intercept_me
[2013-07-09 14:20:08,903](test.py#23)INFO    Will sleep a bit..
[2013-07-09 14:20:13,903](test.py#16)DEBUG   Completed function call. Result => boohoo
[2013-07-09 14:20:13,904](test.py#27)INFO    boohoo
[2013-07-09 14:20:13,904](test.py#28)INFO    Done....
```

Final version
------------------------

Here is the [latest version of the code](https://github.com/bcambel/pythonarticles/blob/master/examples/decorators/part1/ver2.py)

When you look carefully to the latest version of the sample, you will see the **@wrap(intercepted_function)**
decorator added to our inner function(**timer**). The reason for that is ;

```
Without the use of this decorator factory, the name of the example 
function would have been 'wrapper', 
and the docstring of the original example() would have been lost.
Take a look at the [origin documentation](http://docs.python.org/2/library/functools.html#functools.wraps)
```

```python
import time
import logging
import random 
from functools import wraps
from datetime import datetime as dt

logging.basicConfig(format='[%(asctime)s](%(filename)s#%(lineno)d)%(levelname)-7s %(message)s',
                    level=logging.NOTSET)


def intercept_me(intercepted_function):
    @wraps(intercepted_function)
    def timer(*args, **kwargs):
        '''*args and **kwargs are the parameters that are supplied to our original function'''
        # get our actual function name
        function_name = intercepted_function.func_name
        # call our actual function
        # store the return of the function in a parameter
        logging.debug("Starting capturing the time of the executing '%s'" % function_name)
        start = dt.now()
        actual_result = intercepted_function(*args, **kwargs)
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
    logging.info("{0} Starting iter {1}{0}".format(10*"=",i+1))
    logging.info(some_slow_function())

```

Here is the results;
```
[2013-07-09 14:30:56,366](ver2.py#35)INFO    ========== Starting iter 1==========
[2013-07-09 14:30:56,366](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:30:56,366](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:00,367](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:04.001038]
[2013-07-09 14:31:00,367](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:00,367](ver2.py#35)INFO    ========== Starting iter 2==========
[2013-07-09 14:31:00,367](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:00,368](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:02,368](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:02.000702]
[2013-07-09 14:31:02,368](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:02,369](ver2.py#35)INFO    ========== Starting iter 3==========
[2013-07-09 14:31:02,369](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:02,369](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:03,370](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:01.000704]
[2013-07-09 14:31:03,370](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:03,370](ver2.py#35)INFO    ========== Starting iter 4==========
[2013-07-09 14:31:03,370](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:03,370](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:08,371](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:05.000781]
[2013-07-09 14:31:08,371](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:08,371](ver2.py#35)INFO    ========== Starting iter 5==========
[2013-07-09 14:31:08,371](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:08,371](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:13,372](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:05.000993]
[2013-07-09 14:31:13,373](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:13,373](ver2.py#35)INFO    ========== Starting iter 6==========
[2013-07-09 14:31:13,373](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:13,373](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:14,374](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:01.001138]
[2013-07-09 14:31:14,374](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:14,375](ver2.py#35)INFO    ========== Starting iter 7==========
[2013-07-09 14:31:14,375](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:14,375](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:17,376](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:03.001073]
[2013-07-09 14:31:17,376](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:17,376](ver2.py#35)INFO    ========== Starting iter 8==========
[2013-07-09 14:31:17,376](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:17,376](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:22,378](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:05.001008]
[2013-07-09 14:31:22,378](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:22,378](ver2.py#35)INFO    ========== Starting iter 9==========
[2013-07-09 14:31:22,378](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:22,378](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:27,379](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:05.000956]
[2013-07-09 14:31:27,379](ver2.py#36)INFO    boohoo
[2013-07-09 14:31:27,380](ver2.py#35)INFO    ========== Starting iter 10==========
[2013-07-09 14:31:27,380](ver2.py#17)DEBUG   Starting capturing the time of the executing 'some_slow_function'
[2013-07-09 14:31:27,380](ver2.py#30)INFO    Will sleep a bit..
[2013-07-09 14:31:30,381](ver2.py#22)DEBUG   Function: [some_slow_function] => Took [0:00:03.000916]
[2013-07-09 14:31:30,381](ver2.py#36)INFO    boohoo
```

Shameless plug
-------------
Thanks to [@thijsdezoete](https://github.com/thijsdezoete) for the initial kick in..

Well I literally stole Thijs's initial code and made minor modifications. We were talking about how to implement a 
performance tracker. 
