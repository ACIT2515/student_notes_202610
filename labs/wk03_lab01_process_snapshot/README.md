# Decorators Lab: System Process Snapshot Tool 

## Learning Objectives

In this lab, you will:

- Set up a Python project using `uv` for dependency management
- Create and activate a virtual environment with `uv`
- Install external dependencies using `uv`
- Implement Python decorators with parameters
- Work with decorator factories (decorators that take arguments)
- Use the `@wraps` decorator to preserve function metadata
- Test decorator implementations with pytest

## Overview

Build a system process snapshot tool that lists processes running on your system
and displaying the following information about each:

- Name
- Process ID
- Executable
- Command Line
- Username running under
- % CPU Used
- % Memory Used
- Physical Memory Used

You'll implement decorators to: log process information filter processes so only
the current user's are captured.

The main application already provided in `snapshot.py` and you'll be
implementing missing decorators in `decorators.py`.

## Project Tasks

### Task 1: Initilize Project and Create a Virtual Environment with `uv`

Make sure you have the `uv` tool installed.

Initialize your project and create a virtual environment.

### Task 2: Install Required Dependencies

This project requires the following external dependencies:

- `psutil`: A cross-platform library for retrieving information on running
  processes and system utilization

It has the following development dependencies for testing:

- `pytest`: A python testing library

### Task 3 Write Decorators

You will implement two decorators in `decorators.py`:

#### `@log_processes(filename)` Decorator - **YOU IMPLEMENT THIS**

##### Purpose:

Writes process information to a log file after the decorated function executes.

##### Parameters

- `filename`: Path to log file (default: "processes_snapshot.log")

##### Requirements:

- This is a **decorator factory** (a decorator that takes parameters)
- Open the file in write mode (`"w"`) (i.e. each snapshot is overwrites the
  last)
- Write a timestamp using `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`
- Write the number of processes: `"{timestamp} - {len(processes)} processes"`
- Write a header line with column names: PID, Name, User, CPU%, Mem%, Phys
  Mem(MB), Exe, Cmdline
- For each process, write a formatted row with the process information
- The decorator should return the original process list unchanged
- Use `@wraps(func)` to preserve the original function's metadata

##### ExpectedOutputFormat (in log file):

```
2026-01-20 10:30:45 - 15 processes
=====================================================================================
PID      Name                     User                 CPU%     Mem%  Phys Mem(MB)  Exe                             Cmdline
-------------------------------------------------------------------------------------
1234     python.exe              john_doe            15.50     8.20       512.34    C:\Python310\python.exe         python snapshot.py
5678     chrome.exe              john_doe            12.30     5.70       256.78    C:\Program Files\Google\...     chrome.exe --no-sandbox
...
```

You'll need to access process dictionary fields like:

- `proc['pid']`
- `proc['name']`
- `proc['username']`
- `proc['cpu_percent']`
- `proc['memory_percent']`
- `proc['phys_mem']` (in bytes - divide by `1024**2` to get MB)
- `proc['exe']`
- `proc['cmdline']` (this is a list - use `" ".join()` to make it a string)

#### `@filter_by_current_user` Decorator - **YOU IMPLEMENT THIS**

##### Purpose

Filters the process list to show only processes owned by the current user.

##### Requirements:

- This is a simple decorator (does not take parameters)
- Get the current username using `getpass.getuser()` (need to import `getpass`)
- After the decorated function executes, filter the returned process list
- Keep only processes where the current user is "in" the process username
  - Use `current_user in proc.get("username")` to handle domain users (e.g.,
    "DOMAIN\\username")
  - Check that `proc.get("username")` is not None before checking
- Print a message showing filtering information:
  - `"[Filtering] getting only processes for user: {current_user}"`
  - `"[Filtering] Filtered from {original_count} to {filtered_count} processes"`
- Use `@wraps(func)` to preserve the original function's metadata

##### Behavior

```python
@filter_by_current_user
def get_processes_info():
    # Returns all processes
    return processes

# After decorator:
# - Only processes owned by current user are returned
# - Processes owned by other users or system are excluded
```

##### Hints

- Import the `getpass` module: `import getpass`
- Get current user: `current_user = getpass.getuser()`
- Why use `in` instead of `==`? On some systems (especially Windows with domain
  users), the username in the process might be `"DOMAIN\\thomas_lane"` while
  `getpass.getuser()` returns just `"thomas_lane"`. Using `in` handles both
  cases.
- Use a list comprehension or loop to filter:
  ```python
  filtered = []
  for proc in processes:
      proc_user = proc.get("username")
      if proc_user and current_user in proc_user:
          filtered.append(proc)
  ```

### Task 4 Modify `snapshot.py` To Use Decorators

Apply decorators to the `get_process_info()` function so that:

- It suppresses the errors
- Only the current users processes are returned
- The processes are sorted by "phys_mem" in decending order
- Only 15 processes are returned or logged
- The process information is logged to `process_snapshot.log`

## Project Structure

```
system_snapshot/
├── pyproject.toml           # Project configuration and dependencies
├── README.md                # This file
├── decorators.py        # IMPLEMENT YOUR DECORATORS HERE
├── snapshot.py          # Main application (provided - DO NOT EDIT)
└── test_decorators.py   # Test file (provided)
```

## Running the Application

After implementing the decorators, run the snapshot tool:

```bash
uv run python snapshot.py
```

You should see output like:

```
============================================================
System Resource Process Snapshot
============================================================

Scanning for processes...
(This will take a few seconds to measure CPU usage)

[Filtering] getting only processes for user: thomas_lane
[Filtering] Filtered from 215 to 45 processes
[Sorting] Sorted 45 processes by 'name' (ascending)

================================================================================
PROCESSES
================================================================================

[Process 1]
  Name:            chrome.exe
  PID:             1234
  Executable:      C:\Program Files\Google\Chrome\Application\chrome.exe
  Command Line:    chrome.exe --no-sandbox
  Username:        thomas_lane
  CPU:              2.34% per core
  Memory:           3.45%
  Physical Memory:  512.34 MB

[Process 2]
  Name:            python.exe
  PID:             5678
  ...

============================================================
Total processes found: 45
[!] Process information logged to process_snapshot.log
```

## Testing Your Implementation (Optional)

Run the test suite to verify your decorators work correctly:

```bash
uv run pytest test_decorators.py -v
```

All tests should pass:

```
test_decorators.py::test_suppress_errors PASSED
test_decorators.py::test_suppress_errors_propagates_others PASSED
test_decorators.py::test_log_processes PASSED
test_decorators.py::test_filter_by_current_user PASSED
test_decorators.py::test_sort_processes_by_cpu PASSED
test_decorators.py::test_sort_processes_by_name PASSED
test_decorators.py::test_max_listing_limits_results PASSED
test_decorators.py::test_max_listing_under_limit PASSED
```

To run with coverage:

```bash
uv run pytest test_decorators.py --cov=src --cov-report=term-missing
```

## Process Information Captured

For each process, the tool captures:

- **Name**: Process name (e.g., python.exe)
- **PID**: Process ID
- **Executable**: Full path to executable
- **Command Line**: Command and arguments
- **Status**: Process status (running, sleeping, etc.)
- **Username**: User running the process
- **CPU Usage**: Per-core CPU percentage
- **Memory Usage**: Percentage of total system memory
- **Physical Memory**: Resident Set Size (RSS) in bytes

## Implementation Tips

### Decorator Pattern Review

**Simple Decorator (no parameters):**

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper
```

**Decorator Factory (with parameters):**

```python
from functools import wraps

def my_decorator(param1, param2="default"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Can use param1 and param2 here
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

### Why Use `@wraps(func)`?

The `@wraps(func)` decorator from `functools` preserves the original function's:

- Name (`__name__`)
- Docstring (`__doc__`)
- Module (`__module__`)
- Other metadata

Without it, the decorated function would take on the wrapper's name and
metadata.

### Common Pitfalls

1. **Forgetting to return a value**: Decorators should return the result from
   the wrapped function (unless you specifically want to change it)

2. **Not using `*args` and `**kwargs`\*\*: Your wrapper needs to accept any
   arguments the original function might receive

3. **Decorator factory confusion**: If your decorator takes parameters, you need
   THREE levels:
   - Outer function: Takes decorator parameters
   - Middle function: Takes the function to decorate
   - Inner function: The actual wrapper that gets called

4. **Forgetting `@wraps`**: Always use `@wraps(func)` to preserve function
   metadata

## Debugging Tips

If you're having trouble:

1. **Add print statements** in your decorators to see when they're called
2. **Test decorators individually** before stacking them
3. **Check the tests** - they show exactly what your decorator should do
4. **Review the `suppress_errors` decorator** - it's a complete example

## Understanding Decorator Stacking

In `snapshot.py`, multiple decorators will be stacked:

```python
@log_processes("process_snapshot.log")
@max_listing(20)
@sort_processes("phys_mem", True)
@filter_by_current_user
@suppress_errors(psutil.ZombieProcess, PermissionError, ...)
def get_processes_info():
    ...
```

**Execution order** (bottom to top):

1. `@suppress_errors` runs first, wrapping the original function
1. `@filter_by_current_user` wraps the result from step 1
1. `@sort_processes` wraps the result from step 2
1. `@max_listing` limits the number of processes output
1. `@log_processes` wraps the result from step 3 (outermost)

When `get_processes_info()` is called:

1. `log_processes` wrapper runs
2. Calls `sort_processes` wrapper
3. Calls `filter_by_current_user` wrapper
4. Calls `suppress_errors` wrapper
5. Calls original `get_processes_info()`
6. Returns back up the chain

## Submission

When complete, ensure:

- Virtual environment created
- Dependencies installed
- `@log_processes` decorator implemented and working
- `@filter_by_current_user` decorator implemented and working
- Application runs successfully with `uv run python src/snapshot.py`
- Log file (`process_snapshot.log`) is created and contains process information

## Resources

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [functools.wraps Documentation](https://docs.python.org/3/library/functools.html#functools.wraps)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [pytest Documentation](https://docs.pytest.org/)
