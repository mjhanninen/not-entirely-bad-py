# Not entirely bad Python project

This is a skeleton for Python project.  For my personal reference mostly.

## Features

- Requires only Python 3 on the host
- Uses standard `venv` module for virtual environment
- Uses internal `pip` for virtual environment
- Uses `pip-tools` for package dependency resolution
  - Direct dependencies are expressed in the `requirements.in` file
  - All dependencies are locked with the `requirements.txt` file
- Adds project source directories (for exampe, `./src`) to `sys.path`
- Sports Jupyter notebooks alongside
- Works very well on Windows and with Visual Studio Code too (although
  Powershell scripts are still TBD)

## Key scripts

- `mk-venv.sh`: Create and initialize the virtual environment.
- `with-venv.sh command [arg ...]`: Execute `command` within the virtual
  environment.
- `sh-venv.sh [arg ...]`: Spawn a sub-shell within the virtual environment.
  The arguments, if any, are passed on to the `$SHELL` command.
- `run-nb.sh`: Start a Jupyter notebook server. Needs to be run within the
  virtual environment.
- `clean-nbs.sh`: Clean cell output from the tracked Jupyter notebooks. Needs
  to be run wihitn the virtual environment.

## Getting started

Create and initialize a Python virtual environment for the project.  Among
other things this install `pip` and `pip-tools` into the environment:

```console
$ scripts/mk-venv.sh
```

Check that it works:

```console
$ scripts/with-venv.sh which pip
/path/to/project/virtualenv/bin/pip
```

Open a subshell with the virtual environment activated:

```console
$ scripts/sh-venv.sh
```

You can check that the virtual environment is activated:

```console
$ which pip
/path/to/project/virtualenv/bin/pip
```

Compile dependencies (although there is no need as up-to-date
`requirements.txt` is already checked in to the repository):

```console
$ pip-compile
```

Sync the dependencies installed the virtual environment with the
`requirements.txt` file:

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
