# REST Client Exploration Activity

## Overview

This activity will guide you through understanding a Python project that uses external libraries, environment-based configuration, and decorators. You'll explore modern Python project management and debug code.

## Part 1: Project Structure & Virtual Environments

### Questions

1. **Examine the project directory.** List all the files you see. What is the purpose of each file?

2. **Look for a `.venv` or `.venv` directory.** 
   1. Do you see one? 
   2. What is a virtual environment and why is it important for Python projects?
   3. How does `uv` manage virtual environments differently than `pip` and `venv`?

3. **Explore the `.venv` directory structure:**
   1. Navigate into the `.venv` directory. What subdirectories do you see?
   2. **Windows users:** Look in `.venv\Lib\site-packages`. What do you find there?
   3. **macOS/Linux users:** Look in `.venv/lib/python3.x/site-packages`. What do you find there?
   4. Can you locate the `requests` and `dotenv` packages in this directory?
   5. How do these packages compare in size to the standard library?

4. **Examine the Scripts/bin directory:**
   1. **Windows:** Look in `.venv\Scripts`. What files do you see?
   2. **macOS/Linux:** Look in `.venv/bin`. What files do you see?
   3. What is the `python` or `python.exe` file in this directory?
   4. How is it different from the system Python installation?

5. **Understanding the activate script:**
   1. Find the activation script:
      - **Windows:** `.venv\Scripts\activate.bat` or `activate.ps1`
      - **macOS/Linux:** `.venv/bin/activate`
   2. Open this file in a text editor. What does it do?
   3. What environment variables does it modify?
   4. Look for the line that modifies the `PATH` environment variable. What directory does it add to the PATH?
   5. Why is it important to add this directory to the beginning of the PATH rather than the end?
   6. Try activating the virtual environment manually:
      - **Windows (CMD):** `.venv\Scripts\activate.bat`
      - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
      - **macOS/Linux:** `source .venv/bin/activate`
   7. What changes in your terminal prompt after activation?
   8. Run `which python` (macOS/Linux) or `where python` (Windows). What path do you see?
   9. Run `echo $PATH` (macOS/Linux) or `echo %PATH%` (Windows) before and after activation. What changed?
   10. How does `uv run` differ from manually activating the environment?

6. **VS Code Integration:**
   1. Open the project in VS Code.
   2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the command palette.
   3. Type "Python: Select Interpreter" and press Enter.
   4. What interpreters are listed? Can you see the `.venv` interpreter for this project?
   5. Select the interpreter from `.venv`. What is its full path?
   6. Open a new integrated terminal in VS Code (`Ctrl+`` or `Terminal > New Terminal`).
   7. Is the virtual environment automatically activated? How can you tell?
   8. Run `python --version` in the integrated terminal. What version do you see?
   9. Compare this to running `python --version` in a terminal outside VS Code. Are they the same?

7. **Debugging Configuration in VS Code:**
   1. Create a `.vscode` folder in your project root if it doesn't exist.
   2. Create a `launch.json` file inside `.vscode` with this configuration:
      ```json
      {
          "version": "0.2.0",
          "configurations": [
              {
                  "name": "Python: Current File",
                  "type": "debugpy",
                  "request": "launch",
                  "program": "${file}",
                  "console": "integratedTerminal"
              }
          ]
      }
      ```
   3. Set a breakpoint in `main.py` by clicking to the left of a line number.
   4. Press `F5` to start debugging. Does it use the correct interpreter?
   5. How can you verify which Python interpreter is being used during debugging?
   6. What happens if you select the wrong interpreter? Try it with your system Python.

8. **Find the `pyproject.toml` file.**
   1. What information does this file contain?
   2. How does this file relate to project dependencies?

9. **Run `uv sync` in your terminal.**
   1. What happened?
   2. Where are the dependencies installed?
   3. Try running `uv pip list`. What do you see?

## Part 2: Dependency Management with UV

### Questions

10. **Open `main.py` and identify all `import` statements.**
    1. Which imports are from the Python standard library?
    2. Which imports are external dependencies?

11. **The project uses two external libraries: `requests` and `python-dotenv`.**
    1. How would you add a new dependency using `uv`?
    2. Try running: `uv add <package_name>` with a test package. What changes in your project?
    3. How would you remove a dependency?
    4. After adding a dependency, examine the following:
       - What changes were made to `pyproject.toml`?
       - What changes were made to `uv.lock`?
       - What new directories appear in `.venv/Lib/site-packages` (or `.venv/lib/python3.x/site-packages`)?
       - Why does `uv` update multiple files when adding just one package?

12. **Why use `uv` instead of `pip`?**
    1. Research and list at least 3 advantages of `uv` over traditional `pip`.

## Part 3: Secret Management & Environment Variables

### Questions

13. **Try running `main.py` without creating a `.env` file.**
    ```bash
    uv run main.py
    ```
    1. What error do you get?
    2. Why does this error occur?

14. **Follow the README to create a `.env` file and add your OMDB API key.**
    1. Why is it important to store API keys in a `.env` file instead of hardcoding them in `main.py`?
    2. What would happen if you committed a `.env` file with your API key to a public GitHub repository?

15. **Examine the `.gitignore` file (if present) or create one.**
    1. Should `.env` be in `.gitignore`? Why or why not?
    2. What other files should typically be ignored in a Python project?

16. **Look at how the API key is loaded in `main.py`:**
    ```python
    OMDB_KEY: Final[str | None] = dotenv.dotenv_values(".env")["OMDB_KEY"]
    ```
    1. What does `dotenv.dotenv_values(".env")` return?
    2. Why use `Final` type hint here?
    3. What happens if `OMDB_KEY` is not in your `.env` file?

## Part 4: Understanding the Code Flow

### Questions

17. **Trace the execution of `main.py`:**
    1. What happens when you run the program?
    2. How many API calls are made in the first loop?
    3. How many API calls are made in the second loop?
    4. How can you tell the difference?

18. **Examine the `get_movie_data()` function:**
    1. What HTTP method does it use?
    2. What does `requests.utils.quote(f'"{title}"')` do? Why is it necessary?
    3. What status code indicates a successful HTTP request?
    4. What does the function return if the request fails?

19. **Use the debugger to trace caching behavior:**
    1. Set a breakpoint inside the `caching_wrapper` function at the line `if title in movie_cache:`.
    2. Set another breakpoint at the line `result = func(title)`.
    3. Open the Watch panel in VS Code's debugger (View > Debug or `Ctrl+Shift+D`).
    4. Add the following watch expressions:
       - `title`
       - `movie_cache`
       - `len(movie_cache)`
    5. Press `F5` to start debugging `main.py`.
    6. Step through the first loop iteration by iteration (use `F10` to step over, `F11` to step into).
    7. Observe the watch expressions. What happens to `movie_cache` after each iteration?
    8. When the second loop starts, does the debugger hit the `result = func(title)` breakpoint? Why or why not?
    9. Does this confirm your answer to question 17?
    10. Try using the Debug Console to evaluate expressions like `title in movie_cache` at different breakpoints.

## Part 5: Understanding Decorators

### Questions

20. **What is the `@cache_movie` decorator doing?**
    1. Remove the `@cache_movie` decorator from `get_movie_data()` and run the program.
    2. How does the behavior change?
    3. Re-add the decorator.

21. **Examine the `cache_movie` function structure:**
    1. Why is `movie_cache = {}` defined inside `cache_movie()` but outside `caching_wrapper()`?
    2. What would happen if `movie_cache` was defined inside `caching_wrapper()`?

22. **Create a simple decorator to understand the pattern:**
    
    Add this code to a new file `decorator_test.py`:
    ```python
    def my_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper
    
    @my_decorator
    def say_hello():
        print("Hello!")
    
    say_hello()
    ```
    1. What output do you see?
    2. How is the decorator changing the behavior of `say_hello()`?

23. **Advanced: Modify the cache decorator:**
    1. Add functionality to print cache statistics (how many hits vs misses).

