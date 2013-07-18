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

There are two inner loops in this example. Starting with <code>for i in range(10)</code>, if the current element passes the condition <code>if i % 2 == 0</code> then the second for loop starts to run <code>for j in range(0,i)</code> and as last the element is added to the list <code>[j ...]</code>

<code>[0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]</code>

### Usages


Lets abuse the list comprehensions ; 

#### Search Highlighting

Given a text, replace all the occurences of a keyword with **bold** text, print the lines that contains the keyword and combine them via "..."

```python
>>> text = "Python is a great language to work with. I like python a lot. The reasons are obvious; its simple and elegant. Great to read"
>>> "...".join([sentence.lower().replace("python","<b>python</b>") for sentence in text.split(".") for word in sentence.split(" ") if 'python' in word.lower() ])
'<b>python</b> is a great language to work with... i like <b>python</b> a lot'
```

#### Which sentence to analyze for which words

Let's say you want to write an algorithm that analyzes the words within sentences which contains the search keyword

```python
>>> [ (sent,word) for sent in text.split(".") for word in sent.split(" ") if len(word)> 2 and 'Python' in sent]
[('Python is a great language to work with', 'Python'), ('Python is a great language to work with', 'great'), ('Python is a great language to work with', 'language'), ('Python is a great language to work with', 'work'), ('Python is a great language to work with', 'with')]
```









