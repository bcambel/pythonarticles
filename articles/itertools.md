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

Excepts a iterable(1,2,3) and the length of the combinations(2) in our case.

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


GroupBy
------------

IFilter
-----------

IMap
-----------

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




