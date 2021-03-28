# build

> Auto-generated documentation for [fhmake.build](../../fhmake/build.py) module.

build: Build documentation, requirements.txt, and run poetry build.

- [Fhmake](../README.md#fhmake-index) / [Modules](../README.md#fhmake-modules) / [fhmake](index.md#fhmake) / build
    - [getDependencies](#getdependencies)
    - [getProcVer](#getprocver)
    - [subtaskGenRequirements](#subtaskgenrequirements)
    - [subtaskUpdatePyproject](#subtaskupdatepyproject)
    - [taskBuild](#taskbuild)

## getDependencies

[[find in source code]](../../fhmake/build.py#L30)

```python
def getDependencies() -> dict[(str, typing.Any)]:
```

Get our dependencies as a dictionary.

#### Returns

- `dict[str,` *str]* - [description]

## getProcVer

[[find in source code]](../../fhmake/build.py#L13)

```python
def getProcVer(version: str) -> str:
```

Process a version string. This is pretty opinionated.

#### Arguments

- `version` *str* - the version

#### Returns

- `str` - the processed version

## subtaskGenRequirements

[[find in source code]](../../fhmake/build.py#L39)

```python
def subtaskGenRequirements() -> None:
```

Generate the requirements files.

## subtaskUpdatePyproject

[[find in source code]](../../fhmake/build.py#L70)

```python
def subtaskUpdatePyproject():
```

Update the pyproject.toml file with our shiny new version specifiers.

## taskBuild

[[find in source code]](../../fhmake/build.py#L84)

```python
def taskBuild(kwargs: list[str]) -> None:
```

Run the build task.

#### Arguments

- `kwargs` *list[str]* - additional args
