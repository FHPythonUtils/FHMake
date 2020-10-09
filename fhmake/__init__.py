"""FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build
security: Run some basic security checks that are not run in vscode
publish: Run poetry publish
checkreqs: check our requirements file will work with most recent pkg versions
"""
from shutil import copy, move, rmtree
from glob import glob
import subprocess
from shlex import split
import argparse
from tomlkit import loads
from simplesecurity.plugins import bandit, safety, dodgy, dlint
from simplesecurity.formatter import ansi


def _getPyproject():
	""" get the pyproject data """
	with open("pyproject.toml") as pyproject:
		return loads(pyproject.read())


HELP = "subcommand must be one of [install, build, security, publish, checkreqs]"
PYPROJECT = _getPyproject()
PACKAGE_NAME = PYPROJECT["tool"]["poetry"]["name"]

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


def _build():
	# Generate DOCS
	print(f"{BLD}{UL}{CB}Building{CLS}\n\n{BLD}{UL}{CG}Documentation{CLS}")
	rmtree("./DOCS/")
	print(_doSysExec("pdoc3 ./" + PACKAGE_NAME + " -o ./DOCS --force")[1].replace("\\", "/"))
	for filePath in glob("./DOCS/" + PACKAGE_NAME + "/*"):
		move(filePath, "./DOCS")
	rmtree("./DOCS/" + PACKAGE_NAME)
	move("./DOCS/index.md", "./DOCS/readme.md")
	# Generate requirements.txt
	print(f"{BLD}{UL}{CG}Requirements.txt{CLS}")
	print(_doSysExec("dephell deps convert --envs=main")[1])
	copy("requirements.txt", "requirements_optional.txt")
	with open("requirements.txt", "r+") as reqsFile:
		unfilteredReqs = reqsFile.readlines()
		dependencies = PYPROJECT["tool"]["poetry"]["dependencies"]
		for requirement in dependencies:
			if isinstance(dependencies[requirement], dict) and "optional" in \
			dependencies[requirement] and dependencies[requirement]["optional"]:
				for req in unfilteredReqs:
					if requirement in req:
						unfilteredReqs.remove(req)
		reqsFile.seek(0)
		reqsFile.writelines(unfilteredReqs)
		reqsFile.truncate()
	# Generate setup.py
	print(f"{BLD}{UL}{CG}Setup.py{CLS}")
	print(_doSysExec("dephell deps convert --to setup.py")[1])
	# Generate dist files
	print(f"{BLD}{UL}{CG}Dist files{CLS}")
	print(_doSysExec("poetry build")[1])


def _install():
	print(f"{BLD}{UL}{CB}Installing{CLS}")
	_doSysExec("poetry install")
	print("Done!")


def _security():
	print(ansi(bandit() + safety() + dodgy() + dlint()))


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
