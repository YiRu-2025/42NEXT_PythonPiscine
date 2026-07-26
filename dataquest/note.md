# Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered and changeable. No duplicate members.

## dict = {key1: value1, key2: value2, ...}
a dictionary stores **key->value** pairs, has order, can change, no duplicate key
### dict built-in methods
- d.keys() returns all keys
- d.values() only returns values
- d.items() returns both key and value

## set = {}
a set stores **unique** values, no duplicate, no key, no order, no index.
### set built-in methods
#### Join Sets
There are several ways to join two or more sets in Python.

- The union() and update() methods joins all items from both sets.
You can use the | operator instead of the union() method, and you will get the same result.
e.g.
```python
set4 = set1.union(set2, set3)
set4 = set1 | set2 | set3
```
the difference of update():
1. The update() method inserts all items from one set into another.
2. The update() changes the original set, and does not return a new set.

- The intersection() method keeps ONLY the duplicates.
Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets.
You can use the & operator instead of the intersection() method, and you will get the same result.

Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

- The difference() method keeps the items from the first set that are not in the other set(s).
The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
You can use the - operator instead of the difference() method, and you will get the same result.
Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

- The symmetric_difference() method keeps all items EXCEPT the duplicates.
The symmetric_difference() method will keep only the elements that are NOT present in both sets.
You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.


Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

#### Python - Remove Set Items
To remove an item in a set, use the remove(), or the discard() method.
Note: If the item to remove does not exist, remove() will raise an error.

Remove "banana" by using the discard() method:
Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.

The clear() method empties the set:
The del keyword will delete the set completely:

*a tip: packing and unpacking by adding a \* before the argument*
| Context                                | Meaning                                |
| -------------------------------------- | -------------------------------------- |
| `*args` in a function definition       | **Pack** arguments into a tuple        |
| `func(*args)` in a function call       | **Unpack** a tuple/list into arguments |
| `*a_list` or an iterable datastructure | **Unpack** iterable object             |

# generator
lazy evalution to save the memory. only prepared when asking for it.
a generator use `yield` not `return`
then use `next()` to call it, will show the result one by one til `StopIteration`.
like a water machine, tap it, give some, tap it again, give the same volume of water. Only if call/tap it, it shows the result.
`yield` does not end the function immediately. It suspends it and remembers its state.