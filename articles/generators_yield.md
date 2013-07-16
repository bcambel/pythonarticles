
Have you ever seen the ```yield``` keyword and wondered what is it doing? 

Yield is a special execution flow with some magic inside it. 

When yield keyword detected by the Python compiler, the return of the function becomes a generator

Python internally represent the function as a iterable output which internally contains the next() method or __next__() method to be precise.
