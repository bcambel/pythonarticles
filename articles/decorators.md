Decorators are really nice way of doing some work with or without effecting the actual implementation. 

Let's start with a simple example; say you have functions that takes a bit time to complete, and you want to log 
how much time did it take ?

In this example we will use the following function as the starting point

```python
import time

def some_slow_function():
    time.sleep(int(random.random() * 10))
    return 'boohoo'
```
It will sleep between 1-10 seconds and return **boohoo**. 

Adding some flavor into the mix with the following code; Let's call our slow function 3 times.

```python
for i in range(1,3):
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
    time.sleep(int(random.random() * 10))
    return 'boohoo'

```

As you see ```time_me``` is a function which returns a function which will intercept the call, do or decide something
to do or not. 



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
