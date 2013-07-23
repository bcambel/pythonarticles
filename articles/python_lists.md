# Lists

Python lists are array implementation with dynamic sizing. A list is a sequence of elements. Python enables you to put any type of object into the same list. So it doesn't matter.

Everything starts with the square brackets <code>[]</code>

Lets start with a basic example. Let's say we have a sentence. 

```python
>>> words = ['Python','is','awesome']
```

## Insert

<code>list.append()</code> adds a new element at the end of the list. Since Python list is dynamically sized, we don't need to think about the length of the list

```python
>>> words.append("!")
```

## Delete

Builtin <code>del</code> command helps to remove an element

```python
>>> words.append("testing")
>>> words
['Python','is','awesome','testing']
>>> del words[len(words)-1]
>>> words
['Python','is','awesome']
```
## Last element, splitting items

<code>words[len(words)-1]</code> is not the preffered way. Because we can use **-1**
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

## Length

Lets find out how many elements do we have in our list.. Python builtin function<code>len()</code> helps us as always

```python
>>> len(words)
4
```

## For loop, iteration

Iterating though each element within the list

```python
>>> for word in words:
...		print word
Python
is
awesome
!
```

## Sort

Builtin <code>sorted()</code> method sorts the elements of a list

```python
>>> for word in words:
...		print word
!
awesome
is
Python
```

