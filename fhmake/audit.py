"""audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.
"""

from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path
from sys import exit as sysexit

from .utils import ANSI, NAME, _doSysExec


def getTotalLines() -> int:
	"""Get the total number of lines python files under the project directory.

	Returns
	-------
		int: total number of lines

	"""
	totalLines = 0
	for pyfile in Path.cwd().rglob("*.py"):
		totalLines += sum(1 for _i in pyfile.open("rb"))

	return totalLines


def subtaskScore(totalLines: int) -> None:
	"""Calculate a score for the module files using the total
	number of lines and pylint output.

	Args:
	----
		totalLines (int): total number of lines for /.

	"""
	# Bugs per KSLOC J. E. Gaffney, "Estimating the Number of Faults in Code,"
	# in IEEE Transactions on Software Engineering, vol. SE-10, no. 4, pp.
	# 459-464, July 1984, doi: 10.1109/TSE.1984.5010260.
	averageBugsPerLine = 21 / 1000

	# Define pylint args
	pylintArgs = [
		"--enable=all",
		"--disable=pointless-string-statement,superfluous-parens,bad-continuation,wrong-import-position,unsubscriptable-object, duplicate-code",
		'--indent-string="\\t"',
		"--ignore-patterns=test_.*?py",
		"--argument-naming-style=camelCase",
		"--attr-naming-style=camelCase",
		"--function-naming-style=camelCase",
		"--method-naming-style=camelCase",
		"--variable-naming-style=camelCase",
		"--load-plugins=pylint.extensions.bad_builtin,pylint.extensions.check_elif,pylint.extensions.redefined_variable_type,pylint.extensions.overlapping_exceptions,pylint.extensions.docparams,pylint.extensions.mccabe,pylint.extensions.empty_comment",
	]
	score = (
		len(
			json.loads(
				_doSysExec(
					"pylint --output-format=json " + " ".join(pylintArgs) + f" {NAME.lower()}"
				)[1]
			)
		)
		/ totalLines
		* 100
	) / averageBugsPerLine
	rank = chr(65 + (score > 49) + (score > 99) + (score > 149) + (score > 199))
	print(
		f"{'Bugs':<26} (%) - {rank} {(score*averageBugsPerLine).__round__(1):>5}\n"
		f"{ANSI['B']}{'Compared to Industry':<26} (%) - {rank} {(score).__round__(1):>5}{ANSI['CLR']}"
	)


def getCCGrade(complexity: float) -> str:
	"""Calculate the cc grade from the complexity.

	Args:
	----
		complexity (float): the complexity of a file/ project

	Returns:
	-------
		str: the grade

	"""
	return chr(65 + min(math.floor(complexity / 10.0) + (5 - complexity < 0), 5))


def subtaskDup(totalLines: int) -> None:
	"""Calculate the amount of duplicated code using the total number
	of lines and pylint output.

	Args:
	----
		totalLines (int): total number of lines

	"""
	pylint = json.loads(
		_doSysExec(
			"pylint --output-format=json --disable=all --enable=duplicate-code --min-similarity-lines 1 "
			f" {NAME.lower()}"
		)[1]
	)
	score = sum(message["message"].count("\n") for message in pylint) / totalLines * 100
	rank = chr(65 + (score > 9) + (score > 19))
	print(f"{ANSI['B']}{'Duplicates':<26} (%) - {rank} {score.__round__(1):>5}{ANSI['CLR']}")


def taskAudit(kwargs: list[str]) -> None:
	"""Do the audit task, this includes checking requirements are up to date
	security analysis and code complexity metrics.

	Args:
	----
		kwargs (list[str]): optional args

	"""
	# Total LOC
	totalLines = getTotalLines()

	# Requirements up to date?
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CB']}Outdated Requirements{ANSI['CLR']}")
	checkrequirements = _doSysExec("poetry show --outdated")
	print(checkrequirements[1])

	# Requirements licenses compatible with project?
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CB']}Requirement Licenses{ANSI['CLR']}")
	with subprocess.Popen("licensecheck -0") as process:
		licensecheck = (process.wait(),)

	# Do a security analysis
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CB']}Linting and Security{ANSI['CLR']}")
	ruff = _doSysExec("pre-commit run -a ruff")
	print(ruff[1])
	safety = _doSysExec("pre-commit run -a python-safety-dependencies-check")
	print(safety[1])

	# Code score
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CB']}Score{ANSI['CLR']}")
	subtaskScore(totalLines)

	# Duplication score
	print(f"\n{ANSI['B']}{ANSI['U']}{ANSI['CB']}Duplication{ANSI['CLR']}")
	subtaskDup(totalLines)

	# Warning for non zero output
	if (checkrequirements[0] | licensecheck[0] | ruff[0] | safety[0]) == 1:
		print(
			f"\n{ANSI['B']}{ANSI['CY']}One of the above checks has reported a warning, "
			f"double check the output of these.{ANSI['CLR']}"
		)
	# Pass non zero to fhmake
	if "-0" in kwargs or "--zero" in kwargs:
		sysexit(checkrequirements[0] | licensecheck[0] | ruff[0] | safety[0])
