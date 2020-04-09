# Not entirely bad Python project

This is a skeleton for a Python project.  For my personal reference mostly.

## Features

- Requires only Python 3 on the host
- Uses the standard `venv` module for the virtual environment
- Does not leak packages from the virtual environment
- Uses `pip-tools` for package dependency resolution
  - Direct dependencies are expressed in the `requirements.in` file
  - All dependencies are locked with the `requirements.txt` file
- Adds project source directories (`./src`, `./test`, and `./notebooks`) to
  `sys.path`
- Sports Jupyter notebooks alongside
- (The concept) works very well on Windows and with Visual Studio Code too
  (although Powershell scripts are still TBD)

## Key scripts

- `mk-venv.sh`: Create and initialize the virtual environment.
- `with-venv.sh command [arg ...]`: Execute `command` within the virtual
  environment.
- `sh-venv.sh [arg ...]`: Spawn a sub-shell within the virtual environment.
  The arguments, if any, are passed on to the `$SHELL` command.
- `run-nb.sh`: Start a Jupyter notebook server. **Note:** needs to be run
  within the virtual environment.
- `clean-nbs.sh`: Clean cell output from the tracked Jupyter
  notebooks. **Note:** needs to be run within the virtual environment.

## Getting started

Create and initialize a Python virtual environment for the project.  Among
other things this will install `pip` and `pip-tools` into the environment:

```console
$ scripts/mk-venv.sh
```

Check that the virtual environment works:

```console
$ scripts/with-venv.sh which pip
/path/to/project/virtualenv/bin/pip
```

Open a sub-shell with the virtual environment activated:

```console
$ scripts/sh-venv.sh
```

You can check that the virtual environment is activated and still works:

```console
$ which pip
/path/to/project/virtualenv/bin/pip
```

Compile the dependencies requirements. (Although there is no need to this as
the `requirements.txt` should already be up-to-date):

```console
$ pip-compile
```

Install the dependencies missing from the virtual environment (and uninstall
the redundant ones, if any):

```console
$ pip-sync
```

Run the test program:

```console
$ python -m hello
```

Start the Jupyter Notebook server:

```console
$ scripts/run-nb.sh
```

## Copyright and license information

Copyright © 2020 Matti Hänninen

See the file `LICENSE` for information on the license.
