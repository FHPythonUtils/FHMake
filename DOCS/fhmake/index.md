# fhmake

> Auto-generated documentation for [fhmake](../../fhmake/__init__.py) module.

FredHappyface Makefile for python. Run one of the following subcommands:

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
security: Run some basic security checks
publish: Run poetry publish (interactive)
checkreqs: check the requirements file will work with most recent pkg versions
licensechk: check the licences used by the requirements are compatible with this project

#### Attributes

- `COMMAND_MAP` - Add new subcommands here:: `{'build': _build, 'install': _install, 'securit...`

## cli

[[find in source code]](../../fhmake/__init__.py#L191)

```python
def cli():
```

cli entry point

## genRequirements

[[find in source code]](../../fhmake/__init__.py#L87)

```python
def genRequirements() -> None:
```

Generate the requirements files

## getDependencies

[[find in source code]](../../fhmake/__init__.py#L78)

```python
def getDependencies() -> dict[(str, typing.Union[(str, dict[(str, str)])])]:
```

Get our dependencies as a dictionary

#### Returns

- `dict[str,` *str]* - [description]

## procVer

[[find in source code]](../../fhmake/__init__.py#L60)

```python
def procVer(version: str, calOnly: bool = False) -> str:
```

Process a version string. This is pretty opinionated

#### Arguments

- `version` *str* - the version

#### Returns

- `str` - the processed version

## updatePyproject

[[find in source code]](../../fhmake/__init__.py#L122)

```python
def updatePyproject():
```

Update the pyproject.toml file with our shiny new version specifiers
