"""FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
security: Run some basic security checks
publish: Run poetry publish (interactive)
checkreqs: check the requirements file will work with most recent pkg versions
licensechk: check the licences used by the requirements are compatible with this project
"""
from __future__ import annotations
from sys import stdout

from os import remove
from shutil import move, rmtree
from glob import glob
import subprocess
import typing
import argparse
import tomlkit
import tomlkit.items
from tomlkit import toml_document

stdout.reconfigure(encoding="utf-8")

def _getPyproject() -> toml_document.TOMLDocument:
	""" get the pyproject data """
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
	"""execute a command and check for errors

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


def procVer(version: str, calOnly: bool=False) -> str:
	"""Process a version string. This is pretty opinionated

	Args:
		version (str): the version

	Returns:
		str: the processed version
	"""
	if version.startswith("^"):
		major = int(version[1:].split('.')[0])
		if not calOnly or major > 1990 or major == 0:
			return f"<{major + 2},>={version[1:]}"
		else:
			return f"<{major + 1},>={version[1:]}"
	return version


def getDependencies() -> dict[str, typing.Union[str, dict[str, str]]]:
	"""Get our dependencies as a dictionary

	Returns:
		dict[str, str]: [description]
	"""
	return dict(**_getPyproject()["tool"]["poetry"]["dependencies"])


def genRequirements() -> None:
	"""Generate the requirements files
	"""
	dependencies = getDependencies()
	dependencies.pop("python")
	requirements = []
	requirementsOpt = []
	for requirement in dependencies:
		if isinstance(dependencies[requirement], dict):
			dependent = dependencies[requirement]
			if "optional" in dependent and dependent["optional"]: # type: ignore
				requirementsOpt.append(f"{requirement}" +
				f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}" + # type: ignore
				f"{procVer(dependent['version'])}") # type: ignore
			else:
				requirements.append(f"{requirement}" +
				f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}" + # type: ignore
				f"{procVer(dependent['version'])}") # type: ignore
		else:
			dependent = typing.cast(str, dependencies[requirement])
			requirements.append(f"{requirement}{procVer(dependent)}")
	with open("requirements.txt", "w") as requirementsTxt:
		requirementsTxt.write("\n".join(sorted(requirements)) + "\n")
	with open("requirements_optional.txt", "w") as requirementsTxt:
		requirementsTxt.write("\n".join(sorted(requirements + requirementsOpt)) +
		"\n")
	print("Done!\nTidying up old setup.py")
	try:
		remove("setup.py")
		remove("README.rst")
	except OSError:
		pass
	print("Done!\n")


def updatePyproject():
	"""Update the pyproject.toml file with our shiny new version specifiers
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


def _build():
	# Update pyproject.toml version specifiers
	print(f"{CG}(Replacing poetry version specifiers){CLS}")
	updatePyproject()
	# Deal with manual changes to pyproject.toml
	print(f"{CG}(Refreshing Poetry){CLS}\n")
	_doSysExec("poetry update")
	# Generate DOCS
	print(f"{BLD}{UL}{CB}Building{CLS}\n\n{BLD}{UL}{CG}Documentation{CLS}")
	try:
		rmtree("./DOCS/")
	except FileNotFoundError:
		pass
	print(_doSysExec("fhdoc")[1].replace("\\", "/"))
	# Generate requirements.txt
	print(f"{BLD}{UL}{CG}Requirements.txt{CLS}")
	genRequirements()
	# Generate dist files
	print(f"{BLD}{UL}{CG}Dist files{CLS}")
	print(_doSysExec("poetry build")[1])


def _install():
	print(f"{BLD}{UL}{CB}Installing{CLS}")
	_doSysExec("poetry install")
	print("Done!")


def _security():
	print(_doSysExec("simplesecurity --fast")[1])


def _publish():
	print(f"{BLD}{UL}{CB}Publish{CLS}")
	with subprocess.Popen("poetry publish") as process:
		_ = process.wait()


def _checkRequirements():
	print(f"{BLD}{UL}{CB}Checking Requirements{CLS}")
	print(_doSysExec("checkrequirements")[1])


def _licenseCheck():
	print(f"{BLD}{UL}{CB}Checking Requirement Licenses{CLS}")
	print(_doSysExec("licensecheck")[1])


# Add new subcommands here:
COMMAND_MAP = {"build": _build, "install": _install, "security": _security,
"publish": _publish, "checkreqs": _checkRequirements, "licensechk": _licenseCheck} # yapf: disable
HELP = "subcommand must be one of {}".format(list(COMMAND_MAP.keys()))


def cli():
	""" cli entry point """
	parser = argparse.ArgumentParser(
	description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("subcommand", action="store", help=HELP)
	args = parser.parse_args()
	if args.subcommand in COMMAND_MAP:
		COMMAND_MAP[args.subcommand]()
	else:
		print(HELP)
