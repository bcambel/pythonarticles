# Generators

Generators functions allow you to declare a function that behaves like a iterator.

Why would we like to use a generator ?

```python
# sum of all the numbers from 0 to 10K
# not problematic. Pretty quick operation..
>>> sum(range(10000))
49995000
```
Lets increase our target number from 10K to 100M

```python
'''Sum all the numbers between 0 to 100M'''
# Be aware, your machine will really slow down.
# 100% CPU, ~3.04GB RAM consumed during calculation
>>> python -m timeit 'print sum(range(100000000))'
10 loops, best of 3: 2.84 sec per loop
'''Sum all the numbers between 0 to 100M - Version 2'''
# 100% CPU, ~4MB RAM consumed during calculation
>>> sum(xrange(100000000))
4999999950000000
# 10 loops, best of 3: 1.14 sec per loop
```

What made the huge different between **3GB** vs **4MB** ? ```Generator```


```python
xrange.__doc__
"""xrange(stop) -> xrange object
xrange(start, stop[, step]) -> xrange object
Like range(), but instead of returning a list, returns an object that
generates the numbers in the range on demand.  For looping, this is
slightly faster than range() and more memory efficient.
"""
```

**Generate a range on demand** means here that when the calling function calls the <code>next()</code> function, the xrange
method will keep on generating the next number.