"""build: Build documentation, requirements.txt, and run poetry build."""

from __future__ import annotations

from pathlib import Path
from shutil import copy, rmtree
from typing import Any, cast

import tomlkit
import tomlkit.items

from .utils import ANSI, _doSysExec, _getPyproject, _setPyproject


def getProcVer(version: str) -> str:
	"""Process a version string. This is pretty opinionated.

	Args:
		version (str): the version

	Returns:
		str: the processed version
	"""
	if version.startswith("^"):
		major = int(version[1:].split(".")[0])
		if major > 1990 or major == 0:  # if cal ver or zero ver
			return f"<{major + 2},>={version[1:]}"
		return f"<{major + 1},>={version[1:]}"
	return version


def getDependencies() -> dict[str, Any]:
	"""Get our dependencies as a dictionary.

	Returns:
		dict[str, str]: [description]
	"""
	return dict(**_getPyproject()["tool"]["poetry"]["dependencies"])


def subtaskGenRequirements() -> None:
	"""Generate the requirements files."""
	dependencies = getDependencies()
	dependencies.pop("python")
	requirements = []
	requirementsOpt = []
	for requirement in dependencies:
		if isinstance(dependencies[requirement], dict):
			dependent = dependencies[requirement]
			if "optional" in dependent and dependent["optional"]:
				requirementsOpt.append(
					f"{requirement}"
					+ f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}"
					f"{getProcVer(dependent['version'])}"
				)
			else:
				requirements.append(
					f"{requirement}"
					+ f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}"
					f"{getProcVer(dependent['version'])}"
				)
		else:
			dependent = cast(str, dependencies[requirement])
			requirements.append(f"{requirement}{getProcVer(dependent)}")
	Path("requirements.txt").write_text("\n".join(sorted(requirements)) + "\n", encoding="utf-8")
	Path("requirements_optional.txt").write_text(
		"\n".join(sorted(requirements + requirementsOpt)) + "\n", encoding="utf-8"
	)
	print("Done!\n")


def subtaskUpdatePyproject():
	"""Update the pyproject.toml file with our shiny new version specifiers."""
	pyproject = _getPyproject()
	dependencies = pyproject["tool"]["poetry"]["dependencies"]
	for requirement in dependencies:
		if requirement != "python":
			if isinstance(dependencies[requirement], tomlkit.items.InlineTable):
				dependent = dependencies[requirement]["version"]
				dependencies[requirement]["version"] = getProcVer(dependent)
			else:
				dependencies[requirement] = getProcVer(dependencies[requirement])
	_setPyproject(pyproject)


def taskBuild(kwargs: list[str]) -> None:
	"""Run the build task.

	Args:
		kwargs (list[str]): additional args
	"""
	_ = kwargs  # unused - silence pylint
	# Update pyproject.toml version specifiers
	print(f"{ANSI['CG']}(Replacing poetry version specifiers){ANSI['CLR']}")
	subtaskUpdatePyproject()
	# Deal with manual changes to pyproject.toml
	print(f"{ANSI['CG']}(Refreshing Poetry){ANSI['CLR']}\n")
	_doSysExec("poetry update")
	# Generate DOCS
	print(
		f"{ANSI['B']}{ANSI['U']}{ANSI['CB']}Building{ANSI['CLR']}\n\n{ANSI['B']}"
		f"{ANSI['U']}{ANSI['CG']}Documentation{ANSI['CLR']}"
	)
	rmtree("DOCS", ignore_errors=True)
	docs = "documentation/reference"
	print(_doSysExec(f"handsdown  --cleanup -o {docs}")[1].replace("\\", "/"))

	# Generate requirements.txt
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CG']}Requirements.txt{ANSI['CLR']}")
	subtaskGenRequirements()
	# Generate dist files
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CG']}Dist files{ANSI['CLR']}")
	print(_doSysExec("poetry build")[1])
