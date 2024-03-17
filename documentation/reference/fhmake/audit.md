# Audit

[Fhmake Index](../README.md#fhmake-index) / [Fhmake](./index.md#fhmake) / Audit

> Auto-generated documentation for [fhmake.audit](../../../fhmake/audit.py) module.

- [Audit](#audit)
  - [getCCGrade](#getccgrade)
  - [getTotalLines](#gettotallines)
  - [subtaskDup](#subtaskdup)
  - [subtaskScore](#subtaskscore)
  - [taskAudit](#taskaudit)

## getCCGrade

[Show source in audit.py:77](../../../fhmake/audit.py#L77)

Calculate the cc grade from the complexity.

#### Arguments

----
 - `complexity` *float* - the complexity of a file/ project

#### Returns

-------
 - `str` - the grade

#### Signature

```python
def getCCGrade(complexity: float) -> str: ...
```



## getTotalLines

[Show source in audit.py:16](../../../fhmake/audit.py#L16)

Get the total number of lines python files under the project directory.

Returns
-------
 int: total number of lines

#### Signature

```python
def getTotalLines() -> int: ...
```



## subtaskDup

[Show source in audit.py:92](../../../fhmake/audit.py#L92)

Calculate the amount of duplicated code using the total number
of lines and pylint output.

#### Arguments

----
 - `totalLines` *int* - total number of lines

#### Signature

```python
def subtaskDup(totalLines: int) -> None: ...
```



## subtaskScore

[Show source in audit.py:31](../../../fhmake/audit.py#L31)

Calculate a score for the module files using the total
number of lines and pylint output.

#### Arguments

----
 - `totalLines` *int* - total number of lines for /.

#### Signature

```python
def subtaskScore(totalLines: int) -> None: ...
```



## taskAudit

[Show source in audit.py:113](../../../fhmake/audit.py#L113)

Do the audit task, this includes checking requirements are up to date
security analysis and code complexity metrics.

#### Arguments

----
 - `kwargs` *list[str]* - optional args

#### Signature

```python
def taskAudit(kwargs: list[str]) -> None: ...
```