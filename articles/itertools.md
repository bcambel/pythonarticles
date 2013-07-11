Itertools
====================

Functions creating iterators for efficient looping says [Python documentation](http://docs.python.org/2/library/itertools.html)

Chain
-----------
Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. 
Used for treating consecutive sequences as a single sequence. Equivalent to:

```python
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
```

```python
from itertools import chain

chained_tuples = chain((1,2,3),(4,5,6))
print chained_tuples
print dir(chained_tuples)

while True:
    try:
		print chained_tuples.next()
	except StopIteration:
		print "Done iterating.."
		break
```

will output

```
<itertools.chain object at 0x1004ea750>
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', 
'__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', 'from_iterable', 'next']
1
2
3
4
5
6
Done iterating..
```

Combinations
---------------------

Expects a iterable(1,2,3) and the length of the combinations(2) in our case.

```python
from itertools import combinations

for i in combinations((1,2,3,4,),2):
	print i

for i in combinations((1,2,3,4,),3):
	print i
	
# Console Output
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)
```

Compress
-------------
Assume that **[1,0,1,0,1,1]** list is our truth table. Given a list of elements, select the only onces that the value at the 
truth table is **True**

```python
>>> from itertools import compress
>>> compressed = compress('ABCDEF', [1,0,1,0,1,1])
>>> [i for i in compressed]
['A', 'C', 'E', 'F']
```

GroupBy
------------
We want to print out all the objects which are same type. We supply a list of objects **things** and give a function 
that will be called for each element in the list, and a value will be evaluated. 

In this scenario ```lambda x: x[0]``` gets the first element of the tuple ```("animal", "bear")```, which will return **animal**

```python
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), 
					("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    print 20 * "="
    for thing in group:
        print "A %s is a %s." % (thing[1], key)
```
```
====================
A bear is a animal.
A duck is a animal.
====================
A cactus is a plant.
====================
A speed boat is a vehicle.
A school bus is a vehicle.
```
If you list comprehense the groupby result elements, you will see the elements are reduced to **itertools._grouper object**
which enables us to iterate over the objects. <code>**for thing in group:**</code>
```python
>>> [i for i in groupby(things, lambda x: x[0])]
[('animal', <itertools._grouper object at 0x1024a0210>), ('plant', <itertools._grouper object at 0x1024a0250>), 
('vehicle', <itertools._grouper object at 0x1024a0410>)]
```

IFilter
-----------

As you might already know, Python has a builtin function called **filter**. Filter function accepts a sequence of elements,
elements from iterable returning only those for which the predicate is True.

```python
>>> filter.__doc__
'''filter(function or None, sequence) -> list, tuple, or string
Return those items of sequence for which function(item) is true.  
If function is None, return the items that are true.  
If sequence is a tuple or string, return the same type, else return a list.'''
>>> filter(mod2, range(10))
[1, 3, 5, 7, 9]
>>> '''The difference is filter result is evaluated whereas ifilter won't be 
evaluated till iterated.
'''
>>> from itertools import ifilter
>>> mod2 = lambda x: x%2
>>> even_numbers_gen = ifilter( mod2, range(10) )
>>> print even_numbers_gen, type(even_numbers_gen), dir(even_numbers_gen)
<itertools.ifilter object at 0x1067d4390> <type 'itertools.ifilter'> ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'next']
>>> [i for i in even_numbers_gen]
[1, 3, 5, 7, 9]

```

IMap
-----------


```python
>>> imap.__doc__
'''imap(func, *iterables) --> 
Make an iterator that computes the function using arguments from
each of the iterables.  Like map() except that it returns an iterator instead of a list and 
that it stops when the shortest iterable is exhausted 
instead of filling in None for shorter iterables.'''
>>> [i for i in imap(pow, (2,3,10), (5,2,3))]
[32, 9, 1000]
>>> [i for i in imap(add, (imap(pow, (2,3,10), (5,2,3)) ), (2,2,2))]
[34, 11, 1002]
```

ISlice
-----------

```python
>>> from itertools import *
>>> islice('ABCDEFG', 2)
<itertools.islice object at 0x1099b5cb0>
>>> [i for i in islice('ABCDEFG', 2)]
['A', 'B']
>>> [i for i in islice('ABCDEFG', 2, 2)]
[]
>>> [i for i in islice('ABCDEFG', 2, None)]
['C', 'D', 'E', 'F', 'G']
>>> [i for i in islice('ABCDEFG', 2, None, 2)]
['C', 'E', 'G']
>>> [i for i in islice('ABCDEFG', 0, None, 2)]
['A', 'C', 'E', 'G']
```

IZip
----------

```python
>>> from itertools import izip
>>> [i for i in izip('ABCD', 'xy')]
[('A', 'x'), ('B', 'y')]
>>> [i for i in izip('ABCD', 'xyz')]
[('A', 'x'), ('B', 'y'), ('C', 'z')]
>>> [i for i in izip('ABCD', 'xyz0')]
[('A', 'x'), ('B', 'y'), ('C', 'z'), ('D', '0')]
>>> [i for i in izip('ABCD', 'xyz01')]
[('A', 'x'), ('B', 'y'), ('C', 'z'), ('D', '0')]

```

Permutations
-------------

```python
>>> from itertools import permutations
>>> permutations('ABCD', 2)
<itertools.permutations object at 0x1099b3cb0>
>>> [i for i in permutations('ABCD', 2)]
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
>>> [i for i in permutations('ABCD', 3)]
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> [i for i in permutations(range(3))]
[(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
>>> [i for i in permutations(range(3),2)]
[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
```

Product
-------------

```python
>>> from itertools import product
>>> product('ABCD', 'xy')
<itertools.product object at 0x109a3f730>
>>> [i for i in product('ABCD', 'xy')]
[('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]
>>> [i for i in product('ABCD', 'xyz')]
[('A', 'x'), ('A', 'y'), ('A', 'z'), ('B', 'x'), ('B', 'y'), ('B', 'z'), ('C', 'x'), ('C', 'y'), ('C', 'z'), ('D', 'x'), ('D', 'y'), ('D', 'z')]
>>> [i for i in product('ABCD', '1')]
[('A', '1'), ('B', '1'), ('C', '1'), ('D', '1')]
```

Repeat
-------------

```python
>>> [i for i in repeat(10, 3)]
[10, 10, 10]
>>> [i for i in repeat("*", 13)]
['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
>>> "".join([i for i in repeat("*", 13)])
'*************'
>>> "*" * 13
'*************'
>>> "".join(repeat("*",13))
'*************'
```

Starmap
------------

```python
>>> from itertools import starmap
>>> starmap(pow, [(2,5), (3,2), (10,3)])
<itertools.starmap object at 0x109a3d1d0>
>>> [i for i in starmap(pow, [(2,5), (3,2), (10,3)])]
[32, 9, 1000]

```
TakeWhile
-----------

```python
>>> >>> takewhile.__doc__
'''takewhile(predicate, iterable) --> takewhile object
Return successive entries from an iterable as long as the 
predicate evaluates to true for each entry.'''
>>> [i for i in takewhile(lambda x: x<5, [1,4,6,4,1])]
[1, 4]
>>> condition = lambda x: x<5
>>> working_list = [1, 4, 6, 4, 1]
>>> [i for i in takewhile(condition,working_list)]
[1, 4]
>>> condition2 = lambda x: True
>>> [i for i in takewhile(condition2,working_list)]
[1, 4, 6, 4, 1]
>>> condition = False
>>> ''' The first parameter is a function which returns True or False, not True/False directly'''
>>> [i for i in takewhile(condition,working_list)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bool' object is not callable
>>> condition = lambda x: False
>>> [i for i in takewhile(condition,working_list)]
[]

```



