
# Python basics - ACIT 2515

# General knowledge

* Python is **strongly** but **dynamically** typed language
* The correct type of a variable **can only be known** at runtime
* Don't look at your editor colors or text decorations to debug your code
* **RUN THE CODE**
* Run your code with `python ...` in the terminal
* Do not use the `Play` button in your editor, unless you know what you are doing
 
# Variables

* Declare, assign, set a variable (save a value): `my_variable = "something"`
* A variable defined inside a function is only "known" within that function (**variable scoping**)
* Global variables are bad. Just don't - use functions, arguments and return values instead
* Use meaningful names for variables. Your variable names should have at least 4 letters.
* Python variables should follow the **snakecase** convention (`my_great_variable`, not `myGreatVariable`)
* Constants should be uppercase: `NUMBER_OF_ATTEMPTS = 2`
* All variables have a type: `type(my_variable)`

<div style="page-break-after: always;"></div>

# [Numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

"Numbers". Transform (= *cast*) one type to the other:

```python
round_number = 20
float_number = 42.4
string_number = "100"

int(float_number)             # 42
int(string_number)            # 100 (not '100' !)
float(round_number)           # 20.0
```

Because of the binary representation of floating point numbers, rouding errors can happen:
```python
0.1 + 0.1 + 0.1 != 0.3
```

* Types: `int`, `float`, `complex`
* Can do arithmetics: `a + b`, `a - b`, `a * b`, `a / b`
* Integer division and modulo: `14 // 3 == 4`, `14 % 3 == 2` (14 = 4 * 3 + 2)
* Complex math are done with `import math`
* `math.sqrt`, `math.pow`, `math.log`

<div style="page-break-after: always;"></div>

# Booleans: `bool`

* Use `==` to check if two values are equal, `!=` if they are different. **`=` assigns a value to a variable**! See also: [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons).
* A boolean value can only be `True` or `False`. You can combine logic with `and`, `or`, and `not`. See [boolean operators](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not).

```python
rich = True
beautiful = True
attractive = rich and beautiful
```

Remember that `not (A and B)` is `not A or not B`, and is not the same as `not A and not B`!

```python
not_attractive = not (rich and beautiful)
not_attractive = not rich or not beautiful
very_unattractive = not rich and not beautiful
```

Note: `None` is also a built-in value (it is neither `True` nor `False`).

<div style="page-break-after: always;"></div>

# Conditions: `if`

```python
if condition:
    # runs if condition is True
elif another:
    # runs if condition is False and another is True
else:
    # runs if condition is False and another is False
```

There is also a short version (one-liner) for `if` statements.

```python
can_drink = True if age > 19 else False
```

<div style="page-break-after: always;"></div>

# Collections

* "Contain" multiple elements
* Elements can be of different types
* `list`, `tuple`, `set`
* `dict`

# Properties of standard collections

| Collection | Ordered (sortable) | Comments                                                           |
| ---------- | ------------------ | ------------------------------------------------------------------ |
| `list`     | Yes                | Mutable.           |
| `tuple`    | Yes                | **Not mutable**                                                    |
| `set`      | No                 | Mutable. Elements are "unique".                                    |
| `dict`     | No                 | Key-value pairs (similar to hashmaps or arrays in other languages) |

<div style="page-break-after: always;"></div>

# Lists and tuples

* A list is a collection of ordered elements (= sequence).
* Type is `list` or `tuple`.
* Sequences in Python are ordered (= you can sort them).
* Lists can be mutated: you can change the values of the elements.
* Tuples can **NOT** be mutated: you can't change their values once defined.
* `sequence[index]` accesses the element at `index` in `sequence`.
* `append` vs `extend`, `insert`, `copy`, `pop`, `reverse`

### [Common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

### [Operation on mutable sequences](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)

```python
# Lists
my_list = [4, 5, 6]      
another_list = list(1, 2, 3)       # Another way to define a list
my_list.append("something")        # Add an element at the end of the list
my_list[0]                         # Access an element by its position in the list (starts at 0)
my_list[2] = "hello"               # Change values
new_list = my_list + another_list  # Concatenate lists with +
my_list.extend(another_list)       # Similar to above, but modifies in place!

# Tuples
my_tuple = (1, 2, 3)
another_tuple = tuple("hello", "world")
my_tuple[1]                   # like lists
my_tuple[0] = 0               # ERROR! Tuples are immutable
```

# Sets

```python
my_set = set(1, 1, 1, 2, 3)   # Elements are unique - the set contains {1, 2, 3}
another_set = {"hello", "hello"}
s[0]                          # ERROR! Sets are not ordered or indexed
```

<div style="page-break-after: always;"></div>

# Iterate on collections

## Use `for variable in collection`

```python
my_list = [1, 2, 3, 4]
for value in my_list:
    print("Value:", value)
```

Do not iterate with indexes - **AVOID** the following:
```python
# This is BAD - don't do it
my_list = [1, 2, 3, 4]
for idx in range(len(my_list)):
    print("Value:", my_list[idx])
```

# Useful functions / properties

```python
my_list = [1, 2, 3, 4, "hello"]
len(my_list)        # Number of elements in the list
5 in my_list        # False: 5 is not in the list
"hello" in my_list  # True
```

<div style="page-break-after: always;"></div>

# Dictionaries: extremely useful!

* Type is `dict`
* Very useful data type: maps **keys** to **values**.
* **Dictionaries are not ordered. You can NOT sort a Python dictionary.**
* `dictionary[my_key]` access the element at key `my_key` in `dictionary`
* Has methods: `keys()`, `values()`, `items()`, `update`

### [Mapping types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

```python
my_dict = {"hello": "goodbye", 1234: "sunshine"}
my_dict = dict((("hello", "goodbye"), (1234, "sunshine")))

my_dict["hello"]              # 'goodbye'
my_dict["test"] = "something" # Add values to the dict
my_dict[1234] = "rain"        # Keys are unique
my_dict.keys()                # List of keys
my_dict.values()              # List of values
my_dict.items()               # List of key/value pairs
```

# Iterate on dictionaries

```python
for key, value in my_dict.items():
    print("Key:", key, " - Value:", value)

# Similar, by using keys
for key in my_dict.keys():
    print("Key:", key, " - Value:", my_dict[key])

# Not using keys, looping on values only
for value in my_dict.values():
    print("Value:", value)
```

<div style="page-break-after: always;"></div>

# Strings (text)

Strings are very much like "lists of characterers". In Python, **string are immutable** (you cannot change a string, only make a copy with changes).

* Type `str`, defined with single quotes `'text'`, double quotes `"text"`. or triple quotes `"""text"""`
* Useful: `split`, `join`, `upper`, `lower`, `isnumeric`
* Use f-strings: `my_string = f"Hello {name}, nice to meet you!"`
* `"abc de f".split()` => `["abc", "de", "f"]`
* `" ".join(["abc", "de", "f"])` => `"abc de f"`
* See also: [common string operations](https://docs.python.org/3/library/string.html)

### [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

```python
my_string = "hello world"
my_string[0]                  # 'h'
my_string[0] = "H"            # ERROR! Strings are immutable
my_string.upper()             # 'HELLO WORLD'
my_string.split(' ')          # ['hello', 'world']
' '.join(['hello', 'world'])  # 'hello world'
'HELLO WORLD'.lower()         # 'hello world'
'world' in my_string          # True
```

# Iterate on strings like lists

```python
for letter in my_string:
    print(letter)
```

# Convert strings to numbers and vice-versa

```python
my_string = "12345"
int(my_string)          # 12345
another = "abc"
int(another)            # Raises an Exception!
```

### Careful... `123 != "123"`

<div style="page-break-after: always;"></div>

# Functions


- Functions have parameters - and receive arguments.
- They return a value (of any type).

```python
def register_student(student_id, name, international=False, scholarship=False):
    # Do something with the parameters
    return True
``` 

The function `register_student` takes four parameters (or arguments):
- `student_id`, and `name` must be provided in this order. They are *positional* arguments.
- `international` and `scholarship` are *keyword* arguments. They do not have to be provided, because they have a *default value*.

Keyword arguments can be provided in any order by using their names:

```python
register_student("A01209697", "Tim", scholarship=True, international=True)
# This is a valid call, even if the keyword arguments are in a different order!
```

# Return values

* All functions return "something" using the `return` statement.
* If the `return` statement is omitted, the function will `return None` (be careful!)
* A function returns ONE value - but the value can be a collection (list, set, tuple, dictionary, etc)

See also: [functions](https://docs.python.org/3/library/functions.html).

<div style="page-break-after: always;"></div>

# Exceptions

* Errors in the code **raise** exceptions.
* You can also manually and voluntarily raise an exception.
* You can catch exceptions by using `try ... except`.

```python
def say_hello(name):
    if name == "Tim":
        raise RuntimeError("This name is not allowed.")
    return f"Hello {name}."
```

```python
try:
    text = say_hello("Tim")
    print(text)
except RuntimeError:
    print("The name you provided is not allowed")
```

Avoid using "empty" `try / except` statements (without specifying the exception), as they make it hard to debug and are bad practice.

```python
# THIS IS BAD. DO NOT DO THIS.
try:
    result = 1/0
except:
    pass
```

<div style="page-break-after: always;"></div>

# Files and paths

```python
with open("my_file.txt", "r") as fp:
    data = fp.read()
```

* Always use `with`, or remember to close the file (you won't, so use `with`).
* 99.99% of the time, you should use **relative paths**
* `open("C:\\Users\\tguicherd\\Documents\\ACIT2515\\lab.txt")` is most likely wrong (absolute path).
* `open("/home/users/tguicherd/lab.txt")` is most likely wrong (absolute path).
* `open("../data/file.txt")` is suspicious. Are you sure you want to go up the directory tree?
* File extensions do not matter: `whatever.docx` saved from Word is actually a ZIP file.
* File formats are a convenience. A file is a file.
* It is common to distinguish **text files** (contains data that can be printed / read on the screen) and **binary files** (contains data that are not characters).
* Still, there are just *files*.

<div style="page-break-after: always;"></div>

# Python modules and `import`

Use `import` to import another piece of code in your program.

```python
import math

math.sqrt(3)
```

```python
from math import sqrt

sqrt(3)
```

Imports will lookup the modules in the following order:
1. in the standard library
2. (usually) in the current folder
3. see `sys.path` for a list of folders

Typical built-in modules (standard library) to know: `os`, `sys`, `math`, `random`, `csv`, `pathlib`, `json`.
 
<div style="page-break-after: always;"></div>

# Debug your programs

* Use the debugger.
* You may also use `print`, it's better than nothing.
* Whatever tool you use, your brain does the debugging. The tools are here to help, but won't give you the answer.
* Read the error messages. 9 times out of 10, the solution to the problem is on the screen.
* Every time you make a change to your code, **RUN THE CODE**.
* Do not make multiple changes to the code. Fix one problem at a time.

# Docstrings and documentation / comments

* Code without comments is bad code.
* In your functions and files, write docstrings (`"""text ..."""`) to inform users about what your code does.
* Add inline comments to explain complicated steps in your program.

Example:

```python
def my_func(a, b):
    """Takes two arguments and returns their average (sum / 2)"""

    output = float(a) + float(b)    # We force conversion to float
    return output / 2
```

> Developers usually spend up to 2/3 of their time **NOT** writing code, but writing documentation and reading other people's code instead.

<div style="page-break-after: always;"></div>

# Code structure

* Separate code into functions
* Separate functions into modules (Python files)
* Organize modules into packages (files in folders)
* Don't forget about `__init__.py` files for packages!
* Use `if __name__ == "__main":` in your modules, to debug and prevent unwanted code execution.
* Create a single entrypoint in your program, and then use modules / packages to organize the logic.

```
├── component_1
│   ├── __init__.py
│   └── sub_package
│       ├── __init__.py
│       ├── sub_module_1.py
│       └── sub_module_2.py
├── component_2
│   ├── __init__.py
│   └── [... files ...]
├── component_3
│   ├── __init__.py
│   └── [... files ...]
└── main.py
```

<div style="page-break-after: always;"></div>

# Kittens die when you do these things

* Use `try ... except` without specifying the exception you want to catch in the `except` statement.
* Use absolute paths.
* Use mutable default arguments for function parameters (like `[]` or `{}`). See [this page](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument).
* Modify a list while you are iterating over it. See [this page](https://stackoverflow.com/questions/6260089/strange-result-when-removing-item-from-a-list-while-iterating-over-it-in-python).
  * use a list comprehension
  * or copy the list first: `my_copy = my_list.copy()`, `my_copy = my_list[:]`
  * :warning: `my_copy = my_list` does not copy the list!