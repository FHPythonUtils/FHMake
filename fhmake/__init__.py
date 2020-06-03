"""FredHappyface Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build
security: Run some basic security checks that are not run in vscode
publish: Run poetry publish
"""
from os import system
from subprocess import Popen
from shlex import split
import argparse

HELP = "subcommand must be one of [install, build, security, publish]"


def _doSysExec(command):
	"""execute a command and check for errors
	shlex.split can be used to make this safe.
	see https://docs.python.org/3/library/shlex.html#shlex.quote

	Args:
		command (string): commands as a string

	Raises:
		RuntimeWarning: throw a warning should there be a non exit code
	"""
	with Popen(split(command), shell=True) as process:
		exitCode = process.wait()
	if exitCode > 0:
		raise RuntimeWarning(command + " has thrown a non zero exit code, you" +
		" may be missing a dependency")

def cli():
	""" cli entry point """
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("subcommand", action="store", help=HELP)
	args = parser.parse_args()

	if args.subcommand == "build":
		print("Building docs, requirements.txt, setup.py, poetry build")
		_doSysExec("pydoc-markdown > DOCS.md")
		_doSysExec("dephell deps convert --envs=main")
		_doSysExec("dephell deps convert --to setup.py")
		_doSysExec("poetry build")
	elif args.subcommand == "install":
		print("Poetry install")
		_doSysExec("poetry install")
	elif args.subcommand == "security":
		print("Checking deps")
		_doSysExec("poetry export -f requirements.txt | safety check --stdin")
	elif args.subcommand == "publish":
		print("Poetry publish")
		_doSysExec("poetry publish")
	else:
		print(HELP)
