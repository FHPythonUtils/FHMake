# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2021.1.2 - 2021/05/01
- Don't check for duplicate code in the regular grade as this is already checked for.


## 2021.1.1 - 2021/04/16
- If installing fhmake\[full\] we need flake8-polyfill to prevent flake8 from breaking

## 2021.1 - 2021/03/28
- Significant refactoring
- Add score + duplicate to audit (similar to functions provided by codacy)


## 2021 - 2021/03/01
- Bugfix requirements.txt generation.

## 2021 - 2021/03/01
- Wrap dependency checking, security analysis and complexity/ Maintainability
  checking in 'audit'
- Tidy up
- Sorted out some typing

## 2020.5.1 - 2020/10/17
- Bump simplesecurity version

## 2020.5 - 2020/10/15
- Replace pdoc3 with fhdoc

## 2020.4 - 2020/10/15
- Replace Poetry version specifiers with our own when running `build`
- PYPROJECT and POETRY constants have been removed (as we modify the file it
  needs to be reloaded)

## 2020.3.2 - 2020/10/14
- Fix unicode decode error with process.communicate

## 2020.3.1 - 2020/10/12
- set stdout to utf-8
- remove shlex.split as things broke on linux

## 2020.3 - 2020/10/11
- Add licensecheck

## 2020.2.5 - 2020/10/11
- fix py 3.7 and 3.8

## 2020.2.4 - 2020/10/09
- bugfix on remove /docs/ if doesn't exist...

## 2020.2.3 - 2020/10/09
- extras info written to requirements.txt
- add typing

## 2020.2.2 - 2020/10/09
- remove dephell dependency
- don't generate setup.py any more

## 2020.2.1 - 2020/10/08
- bugfixes
- use simplesecurity

## 2020.2 - 2020/10/07
- Some requirements are optional (if installed with something like pipx)
- Optional requirements are now included in `requirements_optional.txt`
  and are excluded from `requirements.txt`

## 2020.1.1 - 2020/07/12
- tomlkit = ">=0.5.11,<0.7"

## 2020.1 - 2020/06/07
- Replace pydoc-markdown with pdoc3

## 2020.0.1 - 2020/06/03
- Add more security checks

## 2020 - 2020/06/03
- First release
