# Virtual Environment: In Depth Explainer

## Purpose

Virtual environment are used to:

1. Avoid system pollution interfering with the operating system Python
   installation
1. Avoid dependency conflicts between projects that require different versions
   of the same package.

Python virtual environments are a way to create isolated environments for Python
projects. They allow you to manage python versions and package dependencies
separately for each project and from the system-wide Python installation.

## Definition

A virtual environment is:

1.  a self-contained directory to contain a Python installation for a particular
    version of Python, and to store any additional packages. The directory
    contains:

    1. `Scripts` directory (Windows) or `bin` directory (Unix-like systems) that
       contains the Python interpreter and scripts installed in the virtual
       environment.

       1. `activate<shell specific extension>`: a script in the above directory
          to modify your PATH environment variable to point to the virtual
          environments copy of Python and update your prompt to show that the
          virtual environment is active.

1.  `Lib` directory (Windows) or `lib` directory (Unix-like systems) that
    contains the standard library packages.
    1. `Lib\site-packages` directory (Windows) or `lib/site-packages` directory
       (Unix-like systems) that contains any additional packages installed in
       the virtual environment.
    1. `include` directory that contains C headers for compiling Python
       extensions.
1.  `pyenv.cfg` is a configuration file for the virtual environment stored in
    the root of the virtual environment directory. It is used by `site.py` to
    setup the environment for the python interpreter. It contains:
    1.  `home`: the path to the Python installation directory used to create the
        virtual environment.
    1.  `include-system-site-packages`: Whether the system wide site-packages
        are to be included in the virtual environment - enabling this
        effectively turns off isolation.
    1.  `versions`: the Python version used in the virtual environment.
    1.  `executable`: the path of the Python executable used to create the
        virtual environment.
    1.  `command`: the CLI command used to create the virtual environment
1.

## What `venv` Changes: Where Python lives and where Modules and Packages are found

When you activate a virtual environment, it modifies your shell's environment to
use the Python interpreter and packages specified in the virtual environment.

During start-up, Python automatically loadas the `site.py` module and calls the
`site.main()` function (though this can be overidden). That function calls
`site.venv()` which handles setting up your Python executable to find modules
and packeges.

Together these functions set up the environment for the interpreter, including: 

   1. Adding site-specific paths to the `sys.path` list, allowing for the discovery of additional modules and packages. 
   1. Configuring the `site-packages` directory, where third-party packages are installed. 
   1. Enabling user site directories, allowing users to install packages in their home
   directories.

When using a virtual environment the site module:

1.  Looks for `pyvenv.cfg` in either the same or parent directory as the running
    executable (which is not resolved, so the location of the symlink is used)
1.  Looks for `include-system-site-packages` in `pyvenv.cfg` to decide whether
    the system `site-packages` directory ends up in `sys.path`
1.  Sets `sys.home` if `home` is found in `pyvenv.cfg`, `sys.home` is used by
    `sysconfig` to acccess Python's configuration information. This is used by
    `distutils` and `pip` to determine where to install packages.

Python uses a specific order to search for modules when an import statement is
executed. This order is as follows:

1. **Built-in Modules**: Python first checks if the module is a built-in module
   (e.g., `sys`, `os`).
2. **Current Directory**: If not found, it checks the current directory (the
   directory from which the script is run).
3. **PYTHONPATH**: Next, it checks the directories listed in the `PYTHONPATH`
   environment variable, if set.
4. **Standard Library**: Finally, it checks the standard library directories.

This search order is controlled by modifying the `sys.path` list in your
script or via a virtual environment.

## `<virtual_env>/Scripts/activate` Script

The `activate` script is used to activate a Python virtual environment.

It preforms the following actions:

1. Modifies the `PATH` environment variable, placing the virtual environment's
   `Scripts`/`bin` directory at the beginning. This ensures that the Python
   interpreter and any scripts installed in the virtual environment are used
   instead of the global Python installation.
1. Sets the `VIRTUAL_ENV` environment variable to the path of the virtual
   environment.
1. Changes the command prompt to indicate that the virtual environment is
   active. This is typically done by prefixing the prompt with the name of the
   virtual environment.
1. Defines and registers a function to deactivate the virtual environment, which
   restores the original `PATH` and `VIRTUAL_ENV` values and resets the command
   prompt.

## References

1. [venv - Creation of virtual environments](https://docs.python.org/3/library/venv.html)
1. [How Virtual Environments Work](https://snarky.ca/how-virtual-environments-work/)
1. [The Python Tutorial - Modules](https://docs.python.org/3/tutorial/modules.html)
