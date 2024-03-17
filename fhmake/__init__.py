"""FredHappyface Makefile for python. Run one of the following subcommands.

install: Poetry install
build: Build documentation, requirements.txt, and run poetry build
publish: Run poetry publish (interactive)
audit: dependency checking, security analysis and complexity/ Maintainability
checking. Use with --fast to speed up the security analysis.
"""

from __future__ import annotations

import argparse

from fhmake.audit import taskAudit
from fhmake.build import taskBuild
from fhmake.install import taskInstall
from fhmake.publish import taskPublish

# Add new subcommands here
COMMAND_MAP = {
	"build": taskBuild,
	"install": taskInstall,
	"publish": taskPublish,
	"audit": taskAudit,
}
HELP = f"subcommand must be one of {list(COMMAND_MAP.keys())}"


def cli() -> None:
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
