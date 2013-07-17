# Unit testing with Mock

[Mock](http://www.voidspace.org.uk/python/mock/index.html) is a nice library designed to help you testing your code. It's extremenly flexible and
easy to start with.

<div class='alert alert-info'>
pip install mock
</div>

One of the biggest problem with the unit testing when you are using Django like framework, the unit testing includes database
stuff which really slows down your unit test's run time and also creates a lot of garbage, and a lot of useless code.
But you don't need to use django unittests to code unit tests in a Django project.

[Mock](http://www.voidspace.org.uk/python/mock/index.html) library helps you to achieve that.
I highly suggest you to also take a look at the <a href='https://factoryboy.readthedocs.org/en/latest/' target='_blank'><code>Factory_Boy</code> library</a>

How to return a value when a method is called ?
-------------------------------------------------------

The <code>return_value</code> attribute ( or keyword argument ) enabled to return a value when a method is called.

Example;

```python
>>> mock = Mock(return_value=None)
>>> mock(1, 2, arg='thing')
>>> mock('some', 'thing', 'else')
>>> mock.assert_any_call(1, 2, arg='thing')
```

How to raise an exception when a method is called ?
-------------------------------------------------------

The <code>side_effect</code> attribute ( or keyword argument ) helps you to raise an exception when a method is called

For example ;

```python
>>> m = MagicMock(side_effect=IndexError)
>>> m(1, 2, 3)
Traceback (most recent call last):
  ...
IndexError
>>> m.mock_calls
[call(1, 2, 3)]
>>> m.side_effect = KeyError('Bang!')
>>> m('two', 'three', 'four')
Traceback (most recent call last):
  ...
KeyError: 'Bang!'
```

How to check if a mocked method is called ? ( Expectation )
-------------------------------------------------------

If you expect a specific method is called with specific argument, use the **assert_called_with** method in your mock object


```python
>>> mock = Mock()
>>> mock.method(1, 2, 3, test='wow')
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_with(1, 2, 3, test='wow')
```

If you expect a method whether called **only one time**, use the **assert_called_once_with** method in your mock object

```python
>>> mock = Mock(return_value=None)
>>> mock('foo', bar='baz')
>>> mock.assert_called_once_with('foo', bar='baz')
>>> mock('foo', bar='baz')
>>> mock.assert_called_once_with('foo', bar='baz')
Traceback (most recent call last):
  ...
AssertionError: Expected to be called once. Called 2 times.
```

The above example calls the mock, and it does not fail at the first time, but after the second call, <code>AssertionError</code>
is raised.


Assert Any Call
----------------
<code>assert_any_call</code>

``python

```

Assert Has Calls
----------------
<code>assert_has_calls</code>

reset_mock
------------

``python

```

configure_mock
---------------

Set attributes on the mock through keyword arguments.

Attributes plus return values and side effects can be set on child mocks using standard dot notation and unpacking a dictionary in the method call:

```python
>>> mock = Mock()
>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock.configure_mock(**attrs)
>>> mock.method()
3
>>> mock.other()
Traceback (most recent call last):
  ...
KeyError
```

Specification
--------------

Mock class has a keyword argument called **spec**. Spec allows you to specify the specification of the mock object.
Anything that does not belong to the specification will create a <code>AttributeError</code>

Example

```python
>>> my_mock = Mock(spec=file)
>>> my_mock.size
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/bcambel/code/cas/lib/python2.7/site-packages/mock.py", line 658, in __getattr__
    raise AttributeError("Mock object has no attribute %r" % name)
AttributeError: Mock object has no attribute 'size'
>>> file
<type 'file'>
>>> dir(file)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__',
'__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush',
'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek',
'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> my_mock.readlines
<Mock name='mock.readlines' id='4421180496'>
>>> my_mock.readliness
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/bcambel/code/cas/lib/python2.7/site-packages/mock.py", line 658, in __getattr__
    raise AttributeError("Mock object has no attribute %r" % name)
AttributeError: Mock object has no attribute 'readliness'
```

As you see our mock object that the shape of the file object type