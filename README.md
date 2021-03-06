[![Github top language](https://img.shields.io/github/languages/top/FHPythonUtils/FHMake.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/ff714fa09a7141ef9f0466073971d853.svg?style=for-the-badge)](https://www.codacy.com/gh/FHPythonUtils/FHMake)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/FHMake.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/FHMake.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/FHMake.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/FHMake.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/FHMake.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/fhmake.svg?style=for-the-badge)](https://pypi.org/project/fhmake/)
[![PyPI Version](https://img.shields.io/pypi/v/fhmake.svg?style=for-the-badge)](https://pypi.org/project/fhmake/)

<!-- omit in toc -->
# FHMake

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

FredHappyface Makefile for python. Run one of the following subcommands:

- install: Poetry install
- build: Build documentation, requirements.txt, and run poetry build
- security: Run some basic security checks
- publish: Run poetry publish (interactive)
- checkreqs: check the requirements file will work with most recent pkg versions
- licensechk: check the licences used by the requirements are compatible with this project
<!-- omit in toc -->
## Table of Contents
- [Changelog](#changelog)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog-1)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)

## Changelog
See the [CHANGELOG](/CHANGELOG.md) for more information.

## Install With PIP

**"Slim" Build:** Install simplesecurity\[full\], poetry, checkrequirements\[full\]
and licensecheck\[full\] with pipx

```python
pip install fhmake
```

**Otherwise:**
```python
pip install fhmake[full]
```

Head to https://pypi.org/project/fhmake/ for more info

## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.9.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.9
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.9 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.9)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## Community Files
### Licence
MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md) for more information.

### Support
Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the [Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md) for more information.
