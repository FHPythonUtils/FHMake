"""FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build
security: Run some basic security checks that are not run in vscode
publish: Run poetry publish
"""
from subprocess import Popen
from shlex import split
import argparse
from platform import system
from tomlkit import loads


def _getPyproject():
	""" get the pyproject data """
	with open("pyproject.toml") as pyproject:
		return loads(pyproject.read())


HELP = "subcommand must be one of [install, build, security, publish]"
PYPROJECT = _getPyproject()
PACKAGE_NAME = PYPROJECT["tool"]["poetry"]["name"]


def _doSysExec(command, failOnNonZero=True):
	"""execute a command and check for errors
	shlex.split can be used to make this safer.
	see https://docs.python.org/3/library/shlex.html#shlex.quote
	Note however, that we can still call _doSysExec with a malicious command
	but this change mitigates command chaining. Ultimately, do not accept user
	input or if you do, escape with shlex.quote(), shlex.join(shlex.split())

	Args:
		command (string): commands as a string
		failOnNonZero (boolean, optional): fail on non zero exit code. Defaults
		to True

	Raises:
		RuntimeWarning: throw a warning should there be a non exit code
	"""
	with Popen(split(command), shell=True) as process:
		exitCode = process.wait()
	if failOnNonZero and exitCode > 0:
		raise RuntimeWarning(
		str(split(command)) + " has thrown a non zero exit code, you" +
		" may be missing a dependency")


def cli():
	""" cli entry point """
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("subcommand", action="store", help=HELP)
	args = parser.parse_args()

	if args.subcommand == "build":
		print("Building docs, requirements.txt, setup.py, poetry build")
		_doSysExec("pdoc3 ./" + PACKAGE_NAME + " -o ./DOCS --force")
		if system() == "Windows": # windows is a snowflake
			_doSysExec("powershell.exe -command mv -force ./DOCS/" + PACKAGE_NAME +
			"/* ./DOCS; rm -r ./DOCS/" + PACKAGE_NAME + ";mv -force ./DOCS/index.md ./DOCS/readme.md")
		else:
			_doSysExec("mv ./DOCS/" + PACKAGE_NAME + "/* ./DOCS; rm -r DOCS/" +
			PACKAGE_NAME + "mv ./DOCS/index.md ./DOCS/readme.md")
		_doSysExec("dephell deps convert --envs=main")
		_doSysExec("dephell deps convert --to setup.py")
		_doSysExec("poetry build")
	elif args.subcommand == "install":
		print("Poetry install")
		_doSysExec("poetry install")
	elif args.subcommand == "security":
		print("Checking deps, and code")
		_doSysExec("poetry export -f requirements.txt | safety check --stdin")
		_doSysExec("dodgy")
		_doSysExec("python -m bandit -li --exclude **/test_*.py -s B322 -r -q .",
		False)
		_doSysExec("python -m flake8 --select=DUO .", False)
	elif args.subcommand == "publish":
		print("Poetry publish")
		_doSysExec("poetry publish")
	else:
		print(HELP)
