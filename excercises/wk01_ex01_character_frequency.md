# Review Programming Exercise 01: Dictionaries, Sets, and Loops

## Structure

Create a solution directory `wk01_ex01`

Create a file called `frequency_analysis.py`.

## Exercise 1.1 - number of occurrences of a letter in a string

In this file, create a Python function `char_freq` that:

- takes a string as its only argument
- returns a dictionary:
  - the keys of the dictionary are the letters that appear in the string
  - for each letter, the associated value in the dictionary is the number of
    occurrences of the letter in the string

Examples:

```
>>> char_freq("aaaa")
{'a': 4}
>>> char_freq("Hello!")
{'H': 1, 'e': 1, 'l': 2, 'o': 1, '!': 1}
```

## Exercise 1.2 - number of occurrences, with filters

Create a function `letter_freq`. This function should reuse the `char_freq`
function. It takes a`str` argument (the string). It must:

- remove spaces
- remove punctuation
- count uppercase and lowercase letters together, but return lowercase letters
  in the result
- it _must_ use the `char_freq` function

_Note_: You want to import and use `string.punctuation`.

Example:

```
>>> letter_freq("Hello world!")
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

### Exercise 1.3 - histogram of letters

Create a function `histogram`. This function return a multi-line list of all
letters in a string, with as many "\*" characters as the number of times that
letter appears in the string. You must use the output from `letter_freq`.

```
>>> print(histogram("Haaaaah"))
h **
a *****
>>> print(histogram("Hello world!"))
h *
e *
l ***
o **
w *
r *
d *
```

### Exercise 1.4 - Create a CLI App

Create a `main()` function that uses `argparse` to create a command-line interface with the following functionality:

- Takes a positional argument `in_string` - the string to process
- Provides three mutually exclusive optional flags:
  - `-c` or `--chars`: Use the `char_freq` function
  - `-l` or `--letters`: Use the `letter_freq` function  
  - `-g` or `--histogram`: Use the `histogram` function (default if no flag specified)

The program should print the input string and the result of the selected operation.

Example usage:

```
python frequency_analysis.py "Hello world!" -c
python frequency_analysis.py "Hello world!" --letters
python frequency_analysis.py "Hello world!"
```

### References
1. [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html#argparse-tutorial)
2. [Argparse Documentation](https://docs.python.org/3/library/argparse.html)
3. [String Constants](https://docs.python.org/3/library/string.html#string-constants)
4. [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)