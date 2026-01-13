# Review Programming Exercise 02: Lists and Files

## Structure

Create a solution directory `wk01_ex02`

Create a file called `contact_processing.py`.

## Exercise 2.1 - Count Total Entries

Copy the provided files (`people_1.txt`, `people_2.exe`, `people_3.py`). **THESE
ARE ALL TEXT FILES!**

Create a function `count_entries`. It takes a filename as argument, and returns
the total number of lines (entries) in the file, including empty lines.

Example:

```python
>>> count_entries("people.txt")
57
```

## Exercise 2.2 - Count Non-Empty Entries

Create a function `count_populated_entries`. It takes a filename as argument, and returns
the number of _non-empty lines_ in the file.

Empty lines are lines that contain only whitespace characters (spaces, tabs, newlines).

Hint: you can use readlines, or read, or split, or use the file as an iterator.

Example:

```python
>>> count_populated_entries("people.txt")
50
```

## Exercise 2.3 - List Unique Entries

Create a function `list_unique` to get a set of unique names from the file. Pay
attention to the data - you want to clean up _whitespace characters_ too! 

Hint: you can use a set to filter out duplicates!

Example:

```python
>>> unique_names = list_unique("people_1.txt")
>>> print(unique_names)
{'Tim', 'John', 'Alice', 'Bob', 'Kim', 'Donald'}
```

## Exercise 2.4 - Create a CLI Application

Create a `main()` function that uses `argparse` to create a command-line interface with the following functionality:

- Takes a positional argument `filename` - the file to process
- Provides four mutually exclusive optional flags:
  - `-a` or `--all`: Count all lines (including empty lines) using `count_entries`
  - `-c` or `--count`: Count non-empty lines only using `count_populated_entries`
  - `-u` or `--unique`: List unique entries (unsorted) using `list_unique`
  - `-s` or `--sorted`: List unique entries sorted alphabetically (default if no flag specified)

The program should print appropriate output based on the selected operation.

Example usage:

```bash
python contact_processing.py people_1.txt -a
# Output: Total lines: 15

python contact_processing.py people_1.txt --count
# Output: Non-empty lines: 12

python contact_processing.py people_1.txt -u
# Output: 
# Unique entries (6 total):
#   Alice
#   Bob
#   Donald
#   John
#   Kim
#   Tim

python contact_processing.py people_1.txt
# Output (default sorted):
# Unique entries sorted (6 total):
#   Alice
#   Bob
#   Donald
#   John
#   Kim
#   Tim
```

### References
1. [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
2. [File Objects](https://docs.python.org/3/glossary.html#term-file-object)
3. [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
4. [Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
5. [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html#argparse-tutorial)
