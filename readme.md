# Lists in Memory

Python treats variables like entries in a dictionary, where the
variable\'s **identifier** is the key, and the variable\'s value is the
value associated with that key. In the case of simply values, this is a
straightforward association with the identify with the value, In the
case of complex objects like lists and tuples which can contain simple
values and even other complex objects, Python stores a **reference** to
the location of that object in memory.

This can lead to some interesting situations. For example, if you want
to reliably change the elements of a list in a loop, you need to
explicitly edit the list rather than using the variable declared in the
loop for each value.

``` python
a = [1, 2, 3, 4]
for element in a:
      # changing the value of element does not affect a
      element = element ** 2
# a is still [1, 2, 3, 4]

# What you probably want is...
for index, element in enumerate(a):
      a[index] = element ** 2
# a is now [1, 4, 9, 16]
```

It\'s also important to be aware that you can introduce **side effects**
in your functions. That is, if your function directly modifies the list,
then that change will be present anywhere that list is referenced.
Luckily, Python generally forces you to be explicit when modifying
underlying data structures. Also, it is helpful to remember that using
immutable structures like tuples can often preclude side effects.

``` python
def nondestructive_function(a: list) -> list:
    a = [item ** 2 for item in a] # creates a new list from a
    return a

def destructive_function(a: list) -> list:
    for index, element in enumerate(a):
        a[index] = element ** 2
    return a

a = [1, 2, 3, 4]
b = nondestructive_function(a)
# a is still [1, 2, 3, 4], b is [1, 4, 9, 16]
c = destructive_function(a)
# both a and c are [1, 4, 9, 16] and a is c
a is c # evaluates to True
```

You can check to see if two variables refer to the same object in memory
by using the `is` operator.

## Copying vs Modifying

We\'ve already encountered functions that sort and reverse sequences
(`sorted` and `reversed`), yet the `list` class contains a `sort` method
and a `reverse` method. The difference between these two sets of
functions is whether a new list is created, or the existing list is
modified \"**in place**\". Note that both of these list methods return
`None`.

``` python
reverse() -> None
    Reverse *IN PLACE*.

sort(key=None, reverse=False) -> None
    Sort *IN PLACE*
```

We can create a **shallow copy** of a list using the `copy` method. A
shallow copy preserves references to other complex objects it finds in a
list rather than copying their contents as well. A **deep copy** would
make a copy of all objects referenced, recursively. This is obviously a
lot more work, and has some potential \"traps\" (what if a list contains
a list that contains itself, for example?). If you really need a deep
copy, there is a module `copy` that contains a function `deepcopy` that
avoids these traps.

``` python
a = [[1, 2], [3, 4], [5, 6]]
b = a.copy()
a is b       # evaluates to False
a[0] is b[0] # evaluates to True
b = a[:]     # equivalent to b = a.copy()
```


# Using Lists

We have a few methods for searching withing a list, namely `count` and
`index`.

``` python
count(value)
    Return number of occurrences of value.

index(value, start=0, stop=9223372036854775807)
    Return first index of value, raises ValueError if not present
```

We have a handful of functions for adding or removing items from a list.

``` python
append(object)
    Append object to the end of the list.

insert(index, object)
    Insert object before index

extend(iterable)
    Extend the list by appending elements from iterable

remove(value)
    Remove first occurrence of value, raises ValueError if not present

pop(index=-1)
    Removes and returns the value at index, potentially raises IndexError

clear()
    Removes all items from the list
```

## Stacks and Queues

One of the more useful things we can do with a list is to use it as a
**stack**​---a First In, Last Out data structure. Stacks are often used
to provide a serial presentation of nested structures like nested lists
or trees. Another way to look at this is turning something that is
straightforwardly recursive into something that can be processed with
iteration.

Alternatively, we can treat a list as a **queue**​---a First In, First
Out data structure. Queues can be used in some of the same situations,
but will change the ordering.




