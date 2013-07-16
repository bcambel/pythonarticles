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

**Generate a range on demand** means that, when the function is called, the <code>__iter__()</code> method
will keep on generating the next number.

At the following piece of code, we will generate maximum 100 numbers, which will be randomly generated.
Concatenate the results via a comma. ( <code> ",".join([]) </code> )
When the <code>iter_test</code> method called directly, it returns a **Generator object**. Python magic!

<script src="https://gist.github.com/spil-bahadir/6007597.js"></script>

```python
>>> import random
>>> def iter_test():
...     max = 100
...     while max > 0:
...             yield int(random.random() * 100)
...             max -= 1
...
>>> iter_test()
<generator object iter_test at 0x106163c30>
>>> ",".join([str(i) for i in iter_test()][:100])
'20,68,65,78,56,23,18,10,47,69,95,58,6,89,19,94,58,56,75,13,37,
73,31,98,82,78,71,32,14,55,38,95,68,18,9,32,61,82,49,75,38,20,17,
3,7,94,99,1,55,22,91,81,40,78,1,71,83,78,89,52,46,42,20,74,96,52,
34,75,26,17,83,96,22,18,80,70,25,35,20,53,0,42,72,54,80,3,92,70,35,53,31,76,41,68,66,23,35,8,20,89'
```
