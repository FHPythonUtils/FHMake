# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

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
