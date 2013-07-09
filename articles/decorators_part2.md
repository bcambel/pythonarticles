In the part 1, we described the most basic usage of the decorators. Decorators are functions that intercepts the actual implementation
and do something. Remember that functions are first class citizens(objects) in Python.

```python
from ver2 import *
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
