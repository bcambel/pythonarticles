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

As you might already know, Python has a builtin function called **filter**. Filter function excepts a sequence of elements,
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
'imap(func, *iterables) --> 
Make an iterator that computes the function using arguments from
each of the iterables.  Like map() except that it returns an iterator instead of a list and 
that it stops when the shortest iterable is exhausted 
instead of filling in None for shorter iterables.'
>>> [i for i in imap(pow, (2,3,10), (5,2,3))]
[32, 9, 1000]
>>> [i for i in imap(add, (imap(pow, (2,3,10), (5,2,3)) ), (2,2,2))]
[34, 11, 1002]
```

ISlice
-----------

IZip
----------

Permutations
-------------

Product
-------------

Repeat
-------------

Starmap
------------

TakeWhile
-----------




