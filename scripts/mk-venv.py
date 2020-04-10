#!/usr/bin/env python3

"""
Create project virtual environment
==================================

- Creates a virtual environment
- Upgrade the environment internal `pip`
- Installs `pip-tools` for dependency resolution
- Adds following directories to `sys.path`
  - `$PROJECT/notebooks`
  - `$PROJECT/src`
  - `$PROJECT/test`
"""

import os
from pathlib import Path
import subprocess
import venv

def resolve_site_packages(path: Path):
    if path.is_dir():
        if path.name == "site-packages":
            return path
        else:
            for child in path.iterdir():
                res = resolve_site_packages(child)
                if res is not None:
                    return res

def run_venv(context, cmd, *args):
    env = dict(os.environ)
    env["VIRTUAL_ENV"] = context.env_dir
    if env.get("PATH"):
        env["PATH"] = context.bin_path + os.pathsep + env["PATH"]
    else:
        env["PATH"] = context.bin_path
    cmdline = [cmd]
    cmdline.extend(args)
    subprocess.call(cmdline, env=env)

def run_pip(context, *args):
    if os.name == "nt":
        py_exe = "py"
    else:
        py_exe = "python3"
    run_venv(context, py_exe, "-m", "pip", *args)

def write_project_pth_file(env_dir: Path, site_packages_dir: Path):
    n_levels = len(site_packages_dir.relative_to(env_dir).parts) + 1
    root_path = "/".join([".."] * n_levels)
    with open(site_packages_dir / "project.pth", "w", encoding="utf-8") as f:
        f.write(f"""\
# Extra paths to be included on the virtual environment's `sys.path`.  See
# https://docs.python.org/3/library/site.html for details.

# Project source directories
{root_path}/notebooks
{root_path}/src
{root_path}/test
""")

class ProjectEnvBuilder(venv.EnvBuilder):

    def __init__(self, *args, **kwargs):
        my_kwargs = {
            "system_site_packages": False,
            "with_pip": True,
            "prompt": "ve",
        }
        my_kwargs.update(kwargs)
        super().__init__(*args, **my_kwargs)

    def post_setup(self, context):
        env_dir = Path(context.env_dir)
        site_packages_dir = resolve_site_packages(env_dir)
        write_project_pth_file(env_dir, site_packages_dir)
        bin_dir = Path(context.bin_path)
        run_pip(context, "install", "--upgrade", "pip")
        run_pip(context, "install", "pip-tools")

if __name__ == "__main__":
    ProjectEnvBuilder().create("virtualenv")
