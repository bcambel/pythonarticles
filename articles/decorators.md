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

some_slow_function()
some_slow_function2()
for i in range(1,10):
  some_slow_function()

```


Thanks to [@thijsdezoete](https://github.com/thijsdezoete) for the kick in..
