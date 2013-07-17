# Unit testing with Mock

[Mock](http://www.voidspace.org.uk/python/mock/index.html) is a nice library designed to help you testing your code. It's extremenly flexible and
easy to start with.

<div class='alert alert-info'>
pip install mock
</div>

One of the biggest problem with the unit testing when you are using Django like framework, the unit testing includes database
stuff which really slows down your unit test's run time and also creates a lot of garbage, and a lot of useless code.
But you don't need to use django unittests to run unit tests in a Django project.

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

If you expect a specific method is called with specific argument, use the <code>assert_called_with</code> method in your mock object


```python
>>> mock = Mock()
>>> mock.method(1, 2, 3, test='wow')
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_with(1, 2, 3, test='wow')
```

If you expect a method whether called **only one time**, use the <code>assert_called_once_with</code> method in your mock object

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


assert_any_call

assert_has_calls

reset_mock

configure_mock

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
