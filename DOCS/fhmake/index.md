# fhmake

> Auto-generated documentation for [fhmake](../../fhmake/__init__.py) module.

FredHappyface Makefile for python. Run one of the following subcommands...

- [Fhmake](../README.md#fhmake-index) / [Modules](../README.md#fhmake-modules) / fhmake
    - [cli](#cli)
    - Modules
        - [\_\_main\_\_](module.md#__main__)
        - [audit](audit.md#audit)
        - [build](build.md#build)
        - [install](install.md#install)
        - [publish](publish.md#publish)
        - [utils](utils.md#utils)

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
publish: Run poetry publish (interactive)
audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.

#### Attributes

- `COMMAND_MAP` - Add new subcommands here:: `{'build': taskBuild, 'install': taskInstall, 'p...`

## cli

[[find in source code]](../../fhmake/__init__.py#L29)

```python
def cli():
```

CLI entry point.
