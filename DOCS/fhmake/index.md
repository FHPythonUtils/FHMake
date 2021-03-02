# fhmake

> Auto-generated documentation for [fhmake](../../fhmake/__init__.py) module.

FredHappyface Makefile for python. Run one of the following subcommands...

- [Fhmake](../README.md#fhmake-index) / [Modules](../README.md#fhmake-modules) / fhmake
    - [cli](#cli)
    - [genRequirements](#genrequirements)
    - [getDependencies](#getdependencies)
    - [procVer](#procver)
    - [updatePyproject](#updatepyproject)
    - Modules
        - [\_\_main\_\_](module.md#__main__)

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
publish: Run poetry publish (interactive)
audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.

#### Attributes

- `COMMAND_MAP` - Add new subcommands here:: `{'build': _build, 'install': _install, 'publish': _publish, 'audit': _audit}`

## cli

[[find in source code]](../../fhmake/__init__.py#L213)

```python
def cli():
```

CLI entry point.

## genRequirements

[[find in source code]](../../fhmake/__init__.py#L90)

```python
def genRequirements() -> None:
```

Generate the requirements files.

## getDependencies

[[find in source code]](../../fhmake/__init__.py#L81)

```python
def getDependencies() -> dict[(str, typing.Any)]:
```

Get our dependencies as a dictionary.

#### Returns

- `dict[str,` *str]* - [description]

## procVer

[[find in source code]](../../fhmake/__init__.py#L64)

```python
def procVer(version: str, calOnly: bool = False) -> str:
```

Process a version string. This is pretty opinionated.

#### Arguments

- `version` *str* - the version

#### Returns

- `str` - the processed version

## updatePyproject

[[find in source code]](../../fhmake/__init__.py#L119)

```python
def updatePyproject():
```

Update the pyproject.toml file with our shiny new version specifiers.
