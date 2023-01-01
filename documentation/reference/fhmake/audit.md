# Audit

[Fhmake Index](../README.md#fhmake-index) /
[Fhmake](./index.md#fhmake) /
Audit

> Auto-generated documentation for [fhmake.audit](../../../fhmake/audit.py) module.

- [Audit](#audit)
  - [getCCGrade](#getccgrade)
  - [getTotalLines](#gettotallines)
  - [subtaskComplexity](#subtaskcomplexity)
  - [subtaskDup](#subtaskdup)
  - [subtaskMaintainability](#subtaskmaintainability)
  - [subtaskScore](#subtaskscore)
  - [taskAudit](#taskaudit)

## getCCGrade

[Show source in audit.py:74](../../../fhmake/audit.py#L74)

Calculate the cc grade from the complexity.

#### Arguments

- `complexity` *float* - the complexity of a file/ project

#### Returns

- `str` - the grade

#### Signature

```python
def getCCGrade(complexity: float) -> str:
    ...
```



## getTotalLines

[Show source in audit.py:16](../../../fhmake/audit.py#L16)

Get the total number of lines python files under the project directory.

#### Returns

- `int` - total number of lines

#### Signature

```python
def getTotalLines() -> int:
    ...
```



## subtaskComplexity

[Show source in audit.py:86](../../../fhmake/audit.py#L86)

Report on the complexity of project files.

#### Signature

```python
def subtaskComplexity() -> None:
    ...
```



## subtaskDup

[Show source in audit.py:113](../../../fhmake/audit.py#L113)

Calculate the amount of duplicated code using the total number
of lines and pylint output.

#### Arguments

- `totalLines` *int* - total number of lines

#### Signature

```python
def subtaskDup(totalLines: int) -> None:
    ...
```



## subtaskMaintainability

[Show source in audit.py:99](../../../fhmake/audit.py#L99)

Report on the maintainability of project files.

#### Signature

```python
def subtaskMaintainability() -> None:
    ...
```



## subtaskScore

[Show source in audit.py:31](../../../fhmake/audit.py#L31)

Calculate a score for the module files using the total
number of lines and pylint output.

#### Arguments

- `totalLines` *int* - total number of lines for /.

#### Signature

```python
def subtaskScore(totalLines: int) -> None:
    ...
```



## taskAudit

[Show source in audit.py:131](../../../fhmake/audit.py#L131)

Do the audit task, this includes checking requirements are up to date
security analysis and code complexity metrics

#### Arguments

- `kwargs` *list[str]* - optional args

#### Signature

```python
def taskAudit(kwargs: list[str]) -> None:
    ...
```


