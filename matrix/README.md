# Description
This project is about virtual environment and package management.
Unlike Born2BeRoot to create a virtual machine, this project focusing on the virtual environment to execute a program.

Known container or package management tool: Conda / Anaconda / Docker

## Project Structure
- ex0: **isolated environment** - how to detect current environment and change to virtual environment
- ex1: **program dependency & package management** - build a data analysis tool that requires external libraries.
- ex2: secure configuration system

# EX0: System Environment & Virtual Env Creation
## import modules: sys, os, site
### sys module -- System-specific parameters and functions
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available. Unless explicitly noted otherwise, all variables are read-only

**sys.base_prefix**

Equivalent to prefix, but referring to the base Python installation.

When running under virtual environment, prefix gets overwritten to the virtual environment prefix. base_prefix, conversely, does not change, and always points to the base Python installation. Refer to Virtual Environments for more information.

**sys.executable**

A string giving the absolute path of the executable binary for the Python interpreter, on systems where this makes sense. If Python is unable to retrieve the real path to its executable, sys.executable will be an empty string or None.

**sys.exit([arg])**

Raise a SystemExit exception, signaling an intention to exit the interpreter.

The optional argument arg can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like. Most systems require it to be in the range 0–127, and produce undefined results otherwise. Some systems have a convention for assigning specific meanings to specific exit codes, but these are generally underdeveloped; Unix programs generally use 2 for command line syntax errors and 1 for all other kinds of errors. If another type of object is passed, None is equivalent to passing zero, and any other object is printed to stderr and results in an exit code of 1. In particular, sys.exit("some error message") is a quick way to exit a program when an error occurs.

Since exit() ultimately “only” raises an exception, it will only exit the process when called from the main thread, and the exception is not intercepted. Cleanup actions specified by finally clauses of try statements are honored, and it is possible to intercept the exit attempt at an outer level.

**sys.modules**

This is a dictionary that maps module names to modules which have already been loaded. This can be manipulated to force reloading of modules and other tricks. However, replacing the dictionary will not necessarily work as expected and deleting essential items from the dictionary may cause Python to fail. If you want to iterate over this global dictionary always use sys.modules.copy() or tuple(sys.modules) to avoid exceptions as its size may change during iteration as a side effect of code or activity in other threads.

**sys.path**

A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.

By default, as initialized upon program startup, a potentially unsafe path is prepended to sys.path (before the entries inserted as a result of PYTHONPATH):
- python -m module command line: prepend the current working directory.
- python script.py command line: prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.
- python -c code and python (REPL) command lines: prepend an empty string, which means the current working directory.

To not prepend this potentially unsafe path, use the -P command line option or the PYTHONSAFEPATH environment variable.

A program is free to modify this list for its own purposes. Only strings should be added to sys.path; all other data types are ignored during import.

See also

    Module site This describes how to use .pth files to extend sys.path.

**sys.prefix**
A string giving the site-specific directory prefix where the platform independent Python files are installed; on Unix, the default is /usr/local. This can be set at build time with the --prefix argument to the configure script. See Installation paths for derived paths.

    Note: If a virtual environment is in effect, this prefix will point to the virtual environment. The value for the Python installation will still be available, via base_prefix. Refer to Virtual Environments for more information.

*Changed in version 3.14*: When running under a virtual environment, prefix and exec_prefix are now set to the virtual environment prefix by the path initialization, instead of site. This means that prefix and exec_prefix always point to the virtual environment, even when site is disabled (-S).

**sys.version**

A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. This string is displayed when the interactive interpreter is started. **Do not extract version information out of it, rather, use version_info and the functions provided by the platform module.**

**sys.version_info**

A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial. All values except releaselevel are integers; the release level is 'alpha', 'beta', 'candidate', or 'final'. The version_info value corresponding to the Python version 2.0 is (2, 0, 0, 'final', 0). The components can also be accessed by name, so sys.version_info[0] is equivalent to sys.version_info.major and so on.

### os — Miscellaneous operating system interfaces
This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.

#### os.path — Common pathname manipulations
**os.path.basename(path, /)**

Return the base name of pathname path. This is the second element of the pair returned by passing path to the function split(). Note that the result of this function is different from the Unix basename program; where basename for '/foo/bar/' returns 'bar', the basename() function returns an empty string ('').

### site — Site-specific configuration hook
**site.getsitepackages(prefixes=None)**

Return a list containing all global site-packages directories.

For each directory present in prefixes (or PREFIXES if prefixes is None), this function will find its site-packages subdirectory depending on the system environment, and will return a list of full paths.

# EX1: dependency management
`pip` installs Python packages. `Poetry` manages a Python project's dependencies, virtual environment, lock file, and packaging.

- Uses pandas for data manipulation
- Uses numpy for numerical computations and to generate your simulated matrix data. It must be the source of your dataset — not hardcoded lists or range().
- Uses matplotlib for visualization

The basic of matplotlib to visualize data:
```python
fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_title("My graph")
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.show()
```
Everything else is an extension of that pattern.

- fig: the entire image/window
- ax: the actual graph to draw things

- operations:
    - ax.plot(x, y): line
    - ax.scatter(x, y)
    - ax.hist(data): histogram
    - ax.bar(categories, values): bar chart
    - ax.imshow(image): image

# EX2: Oracle

A Python configuration management project that demonstrates how to safely handle application settings, API keys, database connection strings, and environment-specific configuration using **environment variables** and **python-dotenv**.

## Overview

The Oracle has access to the Matrix's configuration. In a real application, sensitive configuration such as database credentials and API keys should **not** be hardcoded into source code.

This project demonstrates how to:

* Load configuration from environment variables.
* Use a `.env` file for local development.
* Support separate development and production configurations.
* Validate required configuration variables.
* Handle missing or invalid configuration safely.
* Keep secrets out of version control.

**python-dotenv**
Reads the key,value pair from .env and adds them to environment variable. It is great of managing app settings during development and in production using 12-factor principles.

**.gitignore**

Prevents `.env` and other generated Python files from being committed to version control.

## Configuration

The application requires five environment variables:

| Variable        | Description                                            |
| --------------- | ------------------------------------------------------ |
| `MATRIX_MODE`   | Application environment: `development` or `production` |
| `DATABASE_URL`  | Database/storage connection string                     |
| `API_KEY`       | Secret key used for external services                  |
| `LOG_LEVEL`     | Logging verbosity such as `DEBUG` or `INFO`            |
| `ZION_ENDPOINT` | URL used to connect to the Zion network                |

## Security

### Why `.env` is ignored

The `.env` file may contain secrets such as:

* API keys
* Database passwords
* Database connection strings
* Private service endpoints
* Other deployment credentials

Committing these values to Git could expose them to other developers or, if the repository is public, to the entire internet.

For that reason, `.gitignore` contains:

```gitignore
.env
.env.*
!.env.example
```

This prevents `.env` from being tracked while allowing `.env.example` to be committed.

### Never hardcode secrets

Avoid code like:

```python
API_KEY = "my-real-secret-key"
```

Instead, use:

```python
API_KEY = os.environ["API_KEY"]
```

This allows the secret to be supplied securely by the environment.

## Development vs Production

The project demonstrates environment-specific behavior through `MATRIX_MODE`.

### Development

* Uses local database configuration.
* Uses `DEBUG` logging.
* Loads convenient development values from `.env`.
* Suitable for local testing.

### Production

* Uses production environment variables.
* Uses a production database connection.
* Can use a less verbose logging level such as `INFO`.
* Secrets can be supplied by the deployment environment.
* No production secrets need to be stored in the source repository.
