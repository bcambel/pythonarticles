# Lists

Python list is a collection of elements and based on array. Python enables you to put any type of object into the same list and the size of the list is expaned automatically ( behind the scenes ) so that you don't need to worry. 

Everything starts with the square brackets <code>[]</code>

Lets start with a basic example. Let's say we have a sentence. 

```python
>>> words = ['Python','is','awesome']
```

## Append

<code>list.append()</code> adds a new element to the end of the list. Since Python list is dynamically sized, we don't need to think about the length of the list. List will keep on extending itsself. 

```python
>>> words.append("!")
>>> words
['Python','is','awesome','!']
```

## Length

Lets find out how many elements do we have in our list.. Python builtin function<code>len()</code> helps us as always

```python
>>> len(words)
4
```

## Insert

<code>list.insert(location, element)</code> inserts the elemented into the given location. If the location is larger than the number of elements, inserts the element to the last position.

```python
>>> words = ['Python','is','awesome']
>>> words.insert(12, 'hosting')
>>> words
['Python', 'is', 'awesome', 'hosting']
>>> words = ['Python','is','awesome']
>>> words.insert(1, 'hosting')
>>> words
['Python', 'hosting', 'is', 'awesome']
>>> words
['Python', 'hosting', 'is', 'awesome']
```

## Pop

Deletes the last element from the list and returns it. 

```python
>>> words = ['Python','is','awesome','hosting']
>>> words.pop()  # remove the added hosting, pop used
'hosting'
>>> words
['Python','is','awesome']
```

## Delete

Builtin <code>del</code> command helps to remove an element

```python
>>> words = ['Python','is','awesome']
>>> words.append("testing")
>>> words
['Python','is','awesome','testing']
>>> del words[-1] # Returns None. Check the next section to understand -1..
>>> words
['Python','is','awesome']
```

## Combine two or more lists

You can use <code>+</code> operator to combine lists. None of the given lists are effected from the operation, a new list created. It's a costy operation. Use wisely.

```python
>>> go_words = [ 'Go', 'is', 'also', 'nice']
>>> words + "," + go_words
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list
>>> words + ["."] + go_words  # Don't use this code
['Python', 'is', 'awesome', '.', 'Go', 'is', 'also', 'nice']
```

## Extend

<code>list.extend(sequence)</code> adds the given **sequence** ( list is also a sequence ) to the actual list. The return of the call is <code>None</code>

```python
>>> words = ['Python','is','awesome']
>>> go_words = [ 'Go', 'is', 'also', 'nice']
>>> words.extend(go_words)
>>> words
['Python', 'is', 'awesome', 'Go', 'is', 'also', 'nice']
>>> words.extend((1,2,3))
>>> words
['Python', 'is', 'awesome', 'Go', 'is', 'also', 'nice', 1, 2, 3]
```

<div class='alert alert-danger'><p>Be careful</p></div>

```python
>>> words = words.extend([1,2,3])
>>> words
>>> len(words)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'NoneType' has no len()
```

Nothing is printed, because our list became a **None (Object)**. <code>words[len(words)-1]</code> is not the preffered way. Because we can use **-1**
If you are going to built a programming language, please implement this as a must-to-have.
Java, C#, javascript don't have this feature. I still cannot understand, wtf?!

```python
>>> words[-1]
'awesome'
>>> words[-2]
'is'
>>> words[-3]
'Python'
```

## Slicing - Sublist

<code>list[first:last]</code> slice up the list into a sublist. **Last** is not included!

```python
>>> words = ['Python', 'is', 'awesome', 'Go', 'is', 'also', 'nice', 1, 2, 3]
>>> words[0:3] # beaware 3 is not included!
['Python', 'is', 'awesome']
>>> words[:3] # is also same with [0:3]
['Python', 'is', 'awesome']
```

Since we can use negative indexes, lets find the last 3 elements at the list, and try other variations.

```python
>>> words[-3:]
[1, 2, 3]
>>> words[-3:-1]
[1, 2]
>>> words[-3:0] # were you expecting something else ? :)
[]
```

### 

## For loop, iteration

Iterating though each element within the list

```python
words = ['Python', 'is', 'awesome']
>>> for word in words:
...		print word
Python
is
awesome
```

<h2 id='sort'>Sort</h2>

Builtin <code>sorted()</code> or <code>list.sort()</code> sorts the elements of a list.

```python
>>> for word in sorted(words):
...		print word
!
awesome
is
Python
```

<div class='alert alert-info'> <p> Be aware that <code>list.sort()</code> has a side effect that the 
actual list is sorted and the place of the elements will be changed afterwards
</p>

```python
>>> words = ['Python','is','awesome','testing']
>>> sorted(words)
['Python', 'awesome', 'is', 'testing']
>>> words
['Python', 'is', 'awesome', 'testing']
>>> words.sort()
>>> words
['Python', 'awesome', 'is', 'testing']
```
