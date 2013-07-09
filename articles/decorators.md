Decorators are really nice way of doing some work without effecting the actual implementation. Its similar to wire tapping but 
with additional functionality.

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

# **intercepted_function_reference** is a parameter that will be passed
# by Python before the code works.
def intercept_me(intercepted_function_reference):
    # *args and **kwargs are the parameters that are supplied to our original function
    def timer(*args, **kwargs):
        # call our actual function
        # store the return of the function in a parameter
        actual_result = intercepted_function_reference(*args, **kwargs)
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
def intercept_me(intercepted_function_reference):
    # *args and **kwargs are the parameters that are supplied to our original function
    def timer(*args, **kwargs):
        # call our actual function
        # store the return of the function in a parameter
        print "==I'm the timer within the decorator=intercept_me"
        actual_result = intercepted_function_reference(*args, **kwargs)
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
```
The result of the implementation is as follows. All the decorator related logging statements are DEBUG and the rest is INFO
After **Line#15** the actual call is made which you will get the next (**Line#23**) INFO logging. 
**Boohoo** is printed after the DEBUG statement **line#16** because the return of the function call is used within the 
**line#23** <code>logging.info(some_slow_function())</code>

```
[2013-07-09 14:20:08,903](test.py#14)DEBUG   ==I'm the timer within the decorator=intercept_me
[2013-07-09 14:20:08,903](test.py#23)INFO    Will sleep a bit..
[2013-07-09 14:20:13,903](test.py#16)DEBUG   Completed function call. Result => boohoo
[2013-07-09 14:20:13,904](test.py#27)INFO    boohoo
[2013-07-09 14:20:13,904](test.py#28)INFO    Done....
```



```python
from functools import wraps
from datetime import datetime as dt
import time
import random

def time_me(f):
    @wraps(f)
    def timer(*args, **kwargs):
        start = dt.now()
        # make the call to the actual function and get the result
        res = f(*args, **kwargs)
        stop = dt.now()
        execution_time = stop - start
        print 'Function: [{fnc}] => [{timed}]'.format(fnc=f.func_name, timed=execution_time)
        return res
    return timer

@time_me
def some_slow_function():
    time.sleep(int(random.random() * 10))
    print 'Hello world!'
    return 'boohoo'

@time_me
def some_slow_function2():
    time.sleep(2)
    print 'Hello world 22!'
    return 'boohoo 222'


for i in range(0,10):
  some_slow_function()

some_slow_function2()

```

Here is the results;
```
Hello world!
Function: [some_slow_function] => [0:00:03.000403]
Hello world 22!
Function: [some_slow_function2] => [0:00:02.000421]
Hello world!
Function: [some_slow_function] => [0:00:01.000756]
Hello world!
Function: [some_slow_function] => [0:00:05.000722]
Hello world!
Function: [some_slow_function] => [0:00:08.000489]
```

Shameless plug
-------------
Thanks to [@thijsdezoete](https://github.com/thijsdezoete) for the initial kick in..

Well I literally stole Thijs's initial code and made minor modifications. We were talking about how to implement a 
performance tracker. 
