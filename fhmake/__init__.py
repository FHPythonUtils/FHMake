"""FredHappyface Makefile for python. Run one of the following subcommands...

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
publish: Run poetry publish (interactive)
audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import typing
from sys import exit as sysexit, stdout

import tomlkit
import tomlkit.items
from tomlkit import toml_document

stdout.reconfigure(encoding="utf-8")

PY = "py" if platform.system() == "Windows" else "python3"


def _getPyproject() -> typing.Any:
	"""Get the pyproject data."""
	with open("pyproject.toml", encoding="utf=8") as pyproject:
		return tomlkit.parse(pyproject.read())


def _setPyproject(toml: toml_document.TOMLDocument):
	with open("pyproject.toml", "w", encoding="utf=8") as pyproject:
		pyproject.write(tomlkit.dumps(toml))


BLD = "\033[01m"
CLS = "\033[00m"
UL = "\033[04m"
CB = "\033[36m"
CG = "\033[32m"
CY = "\033[33m"
CR = "\033[31m"
CODE = "\033[100m\033[93m"


def _doSysExec(command: str) -> tuple[int, str]:
	"""Execute a command and check for errors.

	Args:
		command (str): commands as a string
	Raises:
		RuntimeWarning: throw a warning should there be a non exit code
	"""
	with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
	stderr=subprocess.STDOUT, encoding="utf-8", errors="ignore") as process:
		out = process.communicate()[0]
		exitCode = process.returncode
	return exitCode, out


def procVer(version: str, calOnly: bool = False) -> str:
	"""Process a version string. This is pretty opinionated.

	Args:
		version (str): the version

	Returns:
		str: the processed version
	"""
	if version.startswith("^"):
		major = int(version[1:].split('.')[0])
		if not calOnly or major > 1990 or major == 0:
			return f"<{major + 2},>={version[1:]}"
		return f"<{major + 1},>={version[1:]}"
	return version


def getDependencies() -> dict[str, typing.Any]:
	"""Get our dependencies as a dictionary.

	Returns:
		dict[str, str]: [description]
	"""
	return dict(**_getPyproject()["tool"]["poetry"]["dependencies"])


def genRequirements() -> None:
	"""Generate the requirements files.
	"""
	dependencies = getDependencies()
	dependencies.pop("python")
	requirements = []
	requirementsOpt = []
	for requirement in dependencies:
		if isinstance(dependencies[requirement], dict):
			dependent = dependencies[requirement]
			if "optional" in dependent and dependent["optional"]:
				requirementsOpt.append(f"{requirement}"
				+ f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}"
				f"{procVer(dependent['version'])}")
			else:
				requirements.append(f"{requirement}"
				+ f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}"
				f"{procVer(dependent['version'])}")
		else:
			dependent = typing.cast(str, dependencies[requirement])
			requirements.append(f"{requirement}{procVer(dependent)}")
	print("Done!\n")


def updatePyproject():
	"""Update the pyproject.toml file with our shiny new version specifiers.
	"""
	pyproject = _getPyproject()
	dependencies = pyproject["tool"]["poetry"]["dependencies"]
	for requirement in dependencies:
		if requirement != "python":
			if isinstance(dependencies[requirement], tomlkit.items.InlineTable):
				dependent = dependencies[requirement]["version"]
				dependencies[requirement]["version"] = procVer(dependent)
			else:
				dependencies[requirement] = procVer(dependencies[requirement])
	_setPyproject(pyproject)


def _build(unknown: list[str]):
	# Update pyproject.toml version specifiers
	print(f"{CG}(Replacing poetry version specifiers){CLS}")
	updatePyproject()
	# Deal with manual changes to pyproject.toml
	print(f"{CG}(Refreshing Poetry){CLS}\n")
	_doSysExec("poetry update")
	# Generate DOCS
	print(f"{BLD}{UL}{CB}Building{CLS}\n\n{BLD}{UL}{CG}Documentation{CLS}")
	print(_doSysExec("fhdoc --cleanup")[1].replace("\\", "/"))
	# Generate requirements.txt
	print(f"{BLD}{UL}{CG}Requirements.txt{CLS}")
	genRequirements()
	# Generate dist files
	print(f"{BLD}{UL}{CG}Dist files{CLS}")
	print(_doSysExec("poetry build")[1])


def _install(unknown: list[str]):
	print(f"{BLD}{UL}{CB}Installing{CLS}")
	_doSysExec("poetry install")
	print("Done!")


def _publish(unknown: list[str]):
	print(f"{BLD}{UL}{CB}Publish{CLS}")
	with subprocess.Popen("poetry publish") as process:
		_ = process.wait()


def _audit(unknown: list[str]):
	# Requirements up to date?
	print(f"{BLD}{UL}{CB}Checking Requirements{CLS}")
	checkrequirements = _doSysExec("checkrequirements -0")
	print(checkrequirements[1])

	# Requirements licenses compatible with project?
	print(f"{BLD}{UL}{CB}Checking Requirement Licenses{CLS}")
	licensecheck = _doSysExec("licensecheck -0")
	print(licensecheck[1])

	# Do a security analysis
	if "--fast" in unknown or "--skip" in unknown:
		cmd = "simplesecurity --fast -0"
	else:
		cmd = "simplesecurity -0"
	simplesecurity = _doSysExec(cmd)
	print(simplesecurity[1])

	# Complexity/ Maintainability with radon
	radonCCRaw = json.loads(_doSysExec(PY + " -X utf8 -m radon cc -j  . ")[1])
	radonMIRaw = json.loads(_doSysExec(PY + " -X utf8 -m radon mi -j  . ")[1])
	print(f"{BLD}{UL}{CB}Checking Complexity{CLS}")
	for file in radonCCRaw:
		fileStr = file.replace('\\', '/')
		cc = sum([ccRaw["complexity"]
		for ccRaw in radonCCRaw[file]]) / len(radonCCRaw[file])
		rank = chr(min(int(math.ceil(cc / 10.0) or 1) - (1, 0)[5 - cc < 0], 5) + 65)
		print(f"{fileStr} - {rank} {cc}")

	print(f"\n{BLD}{UL}{CB}Checking Maintainability{CLS}")
	for file in radonMIRaw:
		fileStr = file.replace('\\', '/')
		print(f"{fileStr} - {radonMIRaw[file]['rank']} {radonMIRaw[file]['mi']}")

	if (checkrequirements[0] | licensecheck[0] | simplesecurity[0]) == 1:
		print(f"\n{BLD}{CY}One of the above checks has reported a warning, "
		f"double check the output of these.{CLS}")

	if "-0" in unknown or "--zero" in unknown:
		sysexit(checkrequirements[0] | licensecheck[0] | simplesecurity[0])


# Add new subcommands here:
COMMAND_MAP = {"build": _build, "install": _install, "publish": _publish,
"audit": _audit} # yapf: disable
HELP = "subcommand must be one of {}".format(list(COMMAND_MAP.keys()))


def cli():
	"""CLI entry point."""
	parser = argparse.ArgumentParser(
	description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("subcommand", action="store", help=HELP)
	args, unknown = parser.parse_known_args()
	if args.subcommand in COMMAND_MAP:
		COMMAND_MAP[args.subcommand](unknown)
	else:
		print(HELP)
