"""FredHappyface Makefile for python. Run one of the following subcommands...

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
publish: Run poetry publish (interactive)
audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.
"""
from __future__ import annotations

import argparse

from .build import taskBuild
from .install import taskInstall
from .publish import taskPublish
from .audit import taskAudit


# Add new subcommands here:
COMMAND_MAP = {
	"build": taskBuild,
	"install": taskInstall,
	"publish": taskPublish,
	"audit": taskAudit,
}
HELP = "subcommand must be one of {}".format(list(COMMAND_MAP.keys()))


def cli():
	"""CLI entry point."""
	parser = argparse.ArgumentParser(
		description=__doc__, formatter_class=argparse.RawTextHelpFormatter
	)
	parser.add_argument("subcommand", action="store", help=HELP)
	args, kwargs = parser.parse_known_args()
	if args.subcommand in COMMAND_MAP:
		COMMAND_MAP[args.subcommand](kwargs)
	else:
		print(HELP)
