# Build

[Fhmake Index](../README.md#fhmake-index) /
[Fhmake](./index.md#fhmake) /
Build

> Auto-generated documentation for [fhmake.build](../../../fhmake/build.py) module.

- [Build](#build)
  - [getDependencies](#getdependencies)
  - [getProcVer](#getprocver)
  - [subtaskGenRequirements](#subtaskgenrequirements)
  - [subtaskUpdatePyproject](#subtaskupdatepyproject)
  - [taskBuild](#taskbuild)

## getDependencies

[Show source in build.py:32](../../../fhmake/build.py#L32)

Get our dependencies as a dictionary.

#### Returns

- `dict[str,` *str]* - [description]

#### Signature

```python
def getDependencies() -> dict[str, Any]:
    ...
```



## getProcVer

[Show source in build.py:15](../../../fhmake/build.py#L15)

Process a version string. This is pretty opinionated.

#### Arguments

- `version` *str* - the version

#### Returns

- `str` - the processed version

#### Signature

```python
def getProcVer(version: str) -> str:
    ...
```



## subtaskGenRequirements

[Show source in build.py:41](../../../fhmake/build.py#L41)

Generate the requirements files.

#### Signature

```python
def subtaskGenRequirements() -> None:
    ...
```



## subtaskUpdatePyproject

[Show source in build.py:72](../../../fhmake/build.py#L72)

Update the pyproject.toml file with our shiny new version specifiers.

#### Signature

```python
def subtaskUpdatePyproject():
    ...
```



## taskBuild

[Show source in build.py:86](../../../fhmake/build.py#L86)

Run the build task.

#### Arguments

- `kwargs` *list[str]* - additional args

#### Signature

```python
def taskBuild(kwargs: list[str]) -> None:
    ...
```

