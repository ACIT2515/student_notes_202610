# ACIT 2515

### Virtual environments

### aka running your Python program

---

# Why virtual environments are useful

* There are different ways of running Python
  * In Windows: py
    * For example: `py -3.10` to run Python3.10
  * In Linux: `python3` (usually)
* Additional libraries are installed using `pip`
  * In Linux: `pip3`

* Use virtual environments
  * Cross platform
  * Repeatable setup
  * Easier to use in the long term
  * Allows separation of dependencies between projects

--- 

# Best practices

* Use the `venv` module from Python
* Create one virtual environment per project / assignment

* The virtual environment will be created in a folder
  * will contain binaries (scripts) to help you work with Python programs
  * will contain the libraries required by your program to run
* The virtual environment folder is typically called `venv` (which makes things even more confusing)
* The virtual environment needs to be **activated** in order to work
* Once your virtual environment is active, the **ONLY** commands you need are `python` and `pip`
* Don't use `py`, `python3`, ...

---

# Making sure your Python install is clean

* Make sure you only have **ONE** version of Python installed on your computer
* Make sure you don't have any Python-related package managers installed (for example: `conda`)
* Make sure you don't use the Python provided by Microsoft Store
* Make sure you use Python installed from the [official package](https://www.python.org/downloads/)
* Make sure your Python version is at least `3.10`
* If any of the above is not true:
  * **uninstall** *everything* related to Python
  * download the official package, and install it
* It looks extreme - but these 15 minutes of work may save you hours of pain later on

---

# Creating a virtual environment

* Create a folder for this course on your computer
* For example: `C:\Users\Tim\BCIT\ACIT2515`
* Open this *folder* in Visual Studio Code
* Open a terminal in VS Code
* Create the virtual environment:
  * `py -m venv venv` (typically in Windows)
  * `python3 -m venv venv` (in Linux)
  * This will run the module `venv` and create a folder called `venv` in `ACIT2515`
  * if you want to create a venv with folder name `tim`, run: `py -m venv tim`

You should only create your virtual environment once, and then only use it (see next slide).

---

# Activating the virtual environment

* To work on your Python project, activate the virtual environment:
  * `.\venv\Scripts\activate.bat` (Windows command line)
  * `.\venv\Scripts\activate.ps1` (Windows Powershell)
  * `source venv/bin/activate` (Linux/macOS)
* Visual Studio Code should also detect the virtual environment and offer to activate automatically: say yes. See next slide for specific Windows issues.

Your prompt will display `venv` when the virtual environment is active.

### From now on, you only want to *open the folder* in VS Code to make sure the venv is active. Do *NOT* right click on files and "Open with VS Code..."

---

# Windows issues

* Activating the virtual environment implies running a "script" on your computer.
* For some reason, Windows thinks this is unsafe and may not allow to do it.
* There should be an error message on the screen. What does it say?
* The error message also contains a link. Did you open the link?
* TL;DR: you want to adjust the execution policy for scripts on your computer
  * `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
  * in PowerShell
* See the [Python documentation](https://docs.python.org/3/library/venv.html)
* See the [Windows documentation](https://go.microsoft.com/fwlink/?LinkID=135170)

---

# Using the virtual environment

* When the virtual environment is active, you can run your Python programs using just `python`.
* You can install additional packages and libraries using `pip`:
  * `pip install pytest` will install the `pytest` library in the virtual environment

<br/>

* When you are done working on your project, use the `deactivate` command to turn off the virtual environment.
  * Nobody does that, though - we just close VS Code instead.

---

# Running a program

* `python my_file.py` is only what you need.
* `python -m XXX` will run the *module* `XXX`
* For example, you can run pytest with `pytest`, or through the module: `python -m pytest`
* The arguments provided are available in `sys.argv`
* `sys.argv` **ALWAYS** contains at least one element
* The first element is always the name of the "script" provided (for example: `my_file.py`)

```python
import sys

print(sys.argv)
```

```bash
$ python my_script.py arg1 arg2 arg3
['my_script.py', 'arg1', 'arg2', 'arg3']
```

---

# Use the interactive Python shell

* You can run a Python module and keep the Python interpreter open
* Useful for debugging

```bash
$ python -i file01.py
Hello from file01!
>>> hello()
Hello.
```

# References
1. [Virtual Environments](https://docs.python.org/3/library/venv.html)
2. [How does python find packages?](https://leemendelowitz.github.io/blog/how-does-python-find-packages.html)