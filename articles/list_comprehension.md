List Comprehension
=======================

It's an easy way to construct lists.

The below examples shows how to add numbers from 0 to 10 into an array and there is nothing wrong with the following piece of code

```python
numbers = []
for i in range(10):
	numbers.append(i)
```

Except, you can do it in one line only

```python
>>> [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The above special sytnax is a neat Python trick to include the elements of a container via a given condition or without any condition. Two important parts of the statement. The first one is;  <code> for i in range(10) </code> our for loop. The second one <code> [i ...]</code> is our way to add elements into the array. 

What if we would like o check if the number is even, do we need to rollback to the first version ? The answer is **No**

```python
>>> even_numbers = [i for i in range(10) if i % 2 == 0]
>>> even_numbers
[0, 2, 4, 6, 8]
```

This time, we have 3 steps. First, <code> for i in range(10) </code> runs. Then our <code>if i % 2 == 0</code> evaluated checking if the number modded to 2. Once the **given condition** is <code>True</code> the <code>[i ...]</code> part is run; the element is added into the end_result array.

Lets add one more step, and find the squares of the each of the even numbers.

```python
>>> even_numbers_squares = [i**2 for i in range(10) if i % 2 == 0]
>>> even_numbers_squares
[0, 4, 16, 36, 64] 
```

Exactly the same run sequence from the previous example, with a additional evaluation with the <code>[i**2]</code> part where we find the square of the even number.

```python
>>> even_numbers_squares_counter = [j for i in range(10) if i % 2 == 0 for j in range(0,i) ]
[0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]
```

<code>[0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]</code>

