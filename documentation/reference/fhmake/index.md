# Fhmake

> Auto-generated documentation for [fhmake](../../../fhmake/__init__.py) module.

FredHappyface Makefile for python. Run one of the following subcommands

- [Fhmake](../README.md#fhmake-index) / [Modules](../MODULES.md#fhmake-modules) / Fhmake
    - [cli](#cli)
    - Modules
        - [Module](module.md#module)
        - [Audit](audit.md#audit)
        - [Build](build.md#build)
        - [Install](install.md#install)
        - [Publish](publish.md#publish)
        - [Utils](utils.md#utils)

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
publish: Run poetry publish (interactive)
audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.

#### Attributes

- `COMMAND_MAP` - Add new subcommands here: `{'build': taskBuild, 'install': taskInstall, 'p...`

## cli

[[find in source code]](../../../fhmake/__init__.py#L28)

```python
def cli():
```

CLI entry point.
