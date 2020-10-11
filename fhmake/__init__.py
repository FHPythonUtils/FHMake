"""FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
security: Run some basic security checks
publish: Run poetry publish (interactive)
checkreqs: check the requirements file will work with most recent pkg versions
licensechk: check the licences used by the requirements are compatible with this project
"""
from __future__ import annotations

from os import remove
from shutil import move, rmtree
from glob import glob
import subprocess
import typing
from shlex import split
import argparse
import tomlkit
from tomlkit import toml_document, items


def _getPyproject() -> toml_document.TOMLDocument:
	""" get the pyproject data """
	with open("pyproject.toml") as pyproject:
		return tomlkit.parse(pyproject.read())


PYPROJECT = _getPyproject()
POETRY = typing.cast(items.Table,
typing.cast(items.Table, PYPROJECT["tool"])["poetry"])

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
	shlex.split can be used to make this safer.
	see https://docs.python.org/3/library/shlex.html#shlex.quote
	Note however, that we can still call _doSysExec with a malicious command
	but this change mitigates command chaining. Ultimately, do not accept user
	input or if you do, escape with shlex.quote(), shlex.join(shlex.split())
	Args:
		command (str): commands as a string
	Raises:
		RuntimeWarning: throw a warning should there be a non exit code
	"""
	with subprocess.Popen(split(command), shell=True, stdout=subprocess.PIPE,
	stderr=subprocess.STDOUT, universal_newlines=True) as process:
		out = process.communicate()[0]
		exitCode = process.returncode
	return exitCode, out


def procVer(version: str) -> str:
	"""Process a version string

	Args:
		version (str): the version

	Returns:
		str: the processed version
	"""
	if version.startswith("^"):
		return f"=={version[1:].split('.')[0]}.*,>={version[1:]}"
	return version


def getDependencies() -> dict[str, typing.Union[str, dict[str, str]]]:
	"""Get our dependencies as a dictionary

	Returns:
		dict[str, str]: [description]
	"""
	return dict(**POETRY["dependencies"])


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


def _build():
	# Deal with manual changes to pyproject.toml
	_doSysExec("poetry update")
	packageName = str(POETRY["name"])
	# Generate DOCS
	print(f"{BLD}{UL}{CB}Building{CLS}\n\n{BLD}{UL}{CG}Documentation{CLS}")
	try:
		rmtree("./DOCS/")
	except FileNotFoundError:
		pass
	print(_doSysExec("pdoc3 ./" + packageName + " -o ./DOCS --force")[1]
	.replace("\\", "/")) # yapf: disable
	for filePath in glob("./DOCS/" + packageName + "/*"):
		move(filePath, "./DOCS")
	rmtree("./DOCS/" + packageName)
	move("./DOCS/index.md", "./DOCS/readme.md")
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
	print(_doSysExec("simplesecurity")[1])


def _publish():
	print(f"{BLD}{UL}{CB}Publish{CLS}")
	with subprocess.Popen(split("poetry publish")) as process:
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
