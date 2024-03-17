# Utils

[Fhmake Index](../README.md#fhmake-index) / [Fhmake](./index.md#fhmake) / Utils

> Auto-generated documentation for [fhmake.utils](../../../fhmake/utils.py) module.

- [Utils](#utils)
  - [_doSysExec](#_dosysexec)
  - [_getPyproject](#_getpyproject)
  - [_setPyproject](#_setpyproject)

## _doSysExec

[Show source in utils.py:36](../../../fhmake/utils.py#L36)

Execute a command and check for errors.

#### Arguments

----
 - `command` *str* - commands as a string

#### Raises

------
 - `RuntimeWarning` - throw a warning should there be a non exit code

#### Returns

-------
 - `tuple[int,` *str]* - return code + stdout

#### Signature

```python
def _doSysExec(command: str) -> tuple[int, str]: ...
```



## _getPyproject

[Show source in utils.py:26](../../../fhmake/utils.py#L26)

Get the pyproject data.

#### Signature

```python
def _getPyproject() -> dict: ...
```



## _setPyproject

[Show source in utils.py:31](../../../fhmake/utils.py#L31)

Write the pyproject data back to file.

#### Signature

```python
def _setPyproject(toml: toml_document.TOMLDocument) -> None: ...
```