# Dictionaries

Dictionaries might be one of the most common used data structures in programming. But they are named differently in almost most common languages. In Java they're called <code>HashMap</code>, in .NET <code>KeyValuePair</code>.


## Creating a dictionary

There are two ways to create dictionaries in Python;

```python
>>> mr_jordan = { "name" : "Micheal", "surname" : "Jordan", "nick" : "AirJordan", "status" : "Legend", "age" : 50}
>>> mr_jordan_two = dict(name="Micheal",surname='Jordan',nick="AirJordan",status="Legend",age=50)
```

<code>"name"</code> is the key, and <code>"Michael"</code> is the value of the key. This is why .NET call them KeyValuePairs, and behind the scenes, dictionary objects' keys are stored as hashed, thus in Java they call them HashMaps. 

As you see when you define a dictionary via curly brackets <code>{}</code>, you have to use string declaration syntax for keys as well. 

## How to get the value of a key ?

 There are a number of ways to get the value(s) of a key

```python
>>> mr_jordan['name']
'Michael'
```

there is a side effect when using this version; if the given <code>key</code> does not exist, Python will throw a <code>KeyError</code> exception. I typed the following into the Python REPL, and got the following result

```python
>>> mr_jordan["python_articles"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'python_articles'
```

Python is a straightforward language, if you want to get a value of a key, use <code>get</code> function.

```python
>>> mr_jordan.get("python_articles")
```

will return <code>None</code> so that you won't see anything in the terminal.

```python
>>> mr_jordan.get.__doc__
'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
``` 

The value of a non-existing key is None, Let's specify a default value <code>&lt;no_name&gt;</code>

```python
>>> mr_jordan.get("python_articles","<no_name>")
'<no_name>'
``` 

## Check if a key exist

Dictionaries have **has_key** method which returns a bool value;

```python
>>> mr_jordan.has_key("python_articles")
False
```

but it's not the preferred way. The better way to do it is;

```python
>>> 'python_articles' in mr_jordan
False
>>> 'name' in mr_jordan
True
```

## How to get all the keys within a dictionary ? 

<code>keys</code> method helps you to get all the keys of a dictionary. It returns a list of strings 

```python
>>> mr_jordan.keys()
['status', 'nick', 'surname', 'name']
```

## Updating the value of a key

I made a typo while setting the name of Mr Jordan. Let's fix it.

```python
mr_jordan['name'] = "Michael"
mr_jordan_two['name'] = "Michael"
```

## Adding a new key value to existing Dictionary

It's pretty straight forward as well

```python
mr_jordan['team'] = "Chicago Bulls"
```

adds the key **team** to the dictionary


## Dictionaries inside dictionaries

If you are going to work on any API, you have the understand the nested concept of dictionaries which are inside lists, tuples or in other dictionaries.

Let's add Mr. Jordans work history. Starting with Chicago Bulls

```python
>>> mr_jordan = { "name" : "Micheal", "surname" : "Jordan", "nick" : "AirJordan", "status" : "Legend", "age" : 50 , "team" : { "name" : "Chicago Bulls" , "start_year" : 1984 , "end_year" : 1998 } }
```

Lets get the **start_year** and **end_year** from the dictionary.

```python
>>> mr_jordan['team']['start_year']
```

But Mr. Jordan did not play only for Chicago Bulls

```python
>>> mr_jordan['teams'] = [ {"name" : "Chicago Bulls" , "start_year" : 1984 , "end_year" : 1998 }, { "name" : "Washington Wizards" , "start_year" : 2001 , "end_year" : 2003 } ]
```

Iterate through all the teams that Mr. Jordan played

```python
>>> mr_jordan['teams'] = [ {"name" : "Chicago Bulls" , "start_year" : 1984 , "end_year" : 1998 }, { "name" : "Washington Wizards" , "start_year" : 2001 , "end_year" : 2003 } ]
>>> for team in mr_jordan['teams'] :
...     print team['name'], team['start_year'], team['end_year'] 
... 
Chicago Bulls 1984 1998
Washington Wizards 2001 2003
```

Lets combine our [List Comprehension knowledge](http://pythonarticles.com/list_comprehension.html) with dictionaries. Create an array of array which contains the values and key of the teams data. 

```python
>>> [team.values() for team in mr_jordan['teams']]
[[1998, 1984, 'Chicago Bulls'], [2003, 2001, 'Washington Wizards']]
>>> [team.keys() for team in mr_jordan['teams']]
[['end_year', 'start_year', 'name'], ['end_year', 'start_year', 'name']]
>>> """Rather than using a list, lets use a tuple"""
>>> [tuple(team.values()) for team in mr_jordan['teams']]
[(1998, 1984, 'Chicago Bulls'), (2003, 2001, 'Washington Wizards')]
```

## Delete a key from the dictionary

Our <code>team</code> key became pointless once we set the <code>teams</code> key. Lets remove it

```python
>>> del mr_jordan['team']
>>> mr_jordan
{'status': 'Legend', 'surname': 'Jordan', 'name': 'Micheal', 'age': 50, 'teams': [{'end_year': 1998, 'start_year': 1984, 'name': 'Chicago Bulls'}, {'end_year': 2003, 'start_year': 2001, 'name': 'Washington Wizards'}], 'nick': 'AirJordan'}
```

### Contributors

Thanks to [@thijsdezoete](https://github.com/thijsdezoete)  and thanks Mr. Jordan for being awesome...

<iframe width="560" height="315" src="//www.youtube.com/embed/LAr6oAKieHk" frameborder="0" allowfullscreen></iframe>