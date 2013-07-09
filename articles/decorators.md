Decorators are really nice way of doing some work with or without effecting the actual implementation. 

Let's start with a simple example; say you have functions that takes a bit time to complete, and you want to log 
how much time did it take ?

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


for i in range(1,10):
  some_slow_function()

some_slow_function2()

```

As you see ```time_me``` is a function which returns a function. 

```python
# f is our actual function that is passed by the python. 
# In this case it will be some_slow_function
def time_me(f):
    # *args and **kwargs are the parameters that are supplied to our original function
    def timer(*args, **kwargs):
        # call our actual function
        # store the return of the function in a parameter
        res = f(*args, **kwargs)
        # return the result
        return res
    # return our inner function which will intercept the call
    return timer
    
@time_me
def some_slow_function():
    time.sleep(int(random.random() * 10))
    return 'boohoo'

```

Shameless plug
-------------
Thanks to [@thijsdezoete](https://github.com/thijsdezoete) for the initial kick in..

Well I literally stole Thijs's initial code and made minor modifications. We were talking about how to implement a 
performance tracker. 
