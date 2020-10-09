"""FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build
security: Run some basic security checks that are not run in vscode
publish: Run poetry publish
checkreqs: check our requirements file will work with most recent pkg versions
"""
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


HELP = "subcommand must be one of [install, build, security, publish, checkreqs]"
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


def genRequirements() -> None:
	"""Generate the requirements files
	"""
	dependencies = typing.cast(
	dict[str, typing.Union[str, dict[str, typing.Union[str, str]]]],
	POETRY["dependencies"]).copy()
	dependencies.pop("python")
	requirements = []
	requirementsOpt = []
	for requirement in dependencies:
		if isinstance(dependencies[requirement], dict):
			dependent = typing.cast(dict[str, typing.Union[str, str]],
			dependencies[requirement])
			if "optional" in dependent and dependent["optional"]:
				requirementsOpt.append(f"{requirement}" +
				f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}" +
				f"{procVer(str(dependent['version']))}")
			else:
				requirements.append(f"{requirement}" +
				f"{'['+dependent['extras'][0]+']' if 'extras' in dependent else ''}" +
				f"{procVer(str(dependent['version']))}")
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
		remove("README.rst")
		remove("setup.py")
	except OSError:
		pass
	print("Done!\n")


def _build():
	packageName = str(POETRY["name"])
	# Generate DOCS
	print(f"{BLD}{UL}{CB}Building{CLS}\n\n{BLD}{UL}{CG}Documentation{CLS}")
	rmtree("./DOCS/")
	print(_doSysExec("pdoc3 ./" + packageName +	" -o ./DOCS --force")[1].replace("\\", "/"))
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


def cli():
	""" cli entry point """
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("subcommand", action="store", help=HELP)
	args = parser.parse_args()

	if args.subcommand == "build":
		_build()
	elif args.subcommand == "install":
		_install()
	elif args.subcommand == "security":
		_security()
	elif args.subcommand == "publish":
		_publish()
	elif args.subcommand == "checkreqs":
		_checkRequirements()
	else:
		print(HELP)
