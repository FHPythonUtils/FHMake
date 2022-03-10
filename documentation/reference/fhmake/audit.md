# Audit

> Auto-generated documentation for [fhmake.audit](../../../fhmake/audit.py) module.

audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.

- [Fhmake](../README.md#fhmake-index) / [Modules](../MODULES.md#fhmake-modules) / [Fhmake](index.md#fhmake) / Audit
    - [getCCGrade](#getccgrade)
    - [getTotalLines](#gettotallines)
    - [subtaskComplexity](#subtaskcomplexity)
    - [subtaskDup](#subtaskdup)
    - [subtaskMaintainability](#subtaskmaintainability)
    - [subtaskScore](#subtaskscore)
    - [taskAudit](#taskaudit)

## getCCGrade

[[find in source code]](../../../fhmake/audit.py#L74)

```python
def getCCGrade(complexity: float) -> str:
```

Calculate the cc grade from the complexity.

#### Arguments

- `complexity` *float* - the complexity of a file/ project

#### Returns

- `str` - the grade

## getTotalLines

[[find in source code]](../../../fhmake/audit.py#L16)

```python
def getTotalLines() -> int:
```

Get the total number of lines python files under the project directory.

#### Returns

- `int` - total number of lines

## subtaskComplexity

[[find in source code]](../../../fhmake/audit.py#L86)

```python
def subtaskComplexity() -> None:
```

Report on the complexity of project files.

## subtaskDup

[[find in source code]](../../../fhmake/audit.py#L113)

```python
def subtaskDup(totalLines: int) -> None:
```

Calculate the amount of duplicated code using the total number
of lines and pylint output.

#### Arguments

- `totalLines` *int* - total number of lines

## subtaskMaintainability

[[find in source code]](../../../fhmake/audit.py#L99)

```python
def subtaskMaintainability() -> None:
```

Report on the maintainability of project files.

## subtaskScore

[[find in source code]](../../../fhmake/audit.py#L31)

```python
def subtaskScore(totalLines: int) -> None:
```

Calculate a score for the module files using the total
number of lines and pylint output.

#### Arguments

- `totalLines` *int* - total number of lines for /.

## taskAudit

[[find in source code]](../../../fhmake/audit.py#L131)

```python
def taskAudit(kwargs: list[str]) -> None:
```

Do the audit task, this includes checking requirements are up to date
security analysis and code complexity metrics

#### Arguments

- `kwargs` *list[str]* - optional args
