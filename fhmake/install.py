"""install: Poetry install."""

from __future__ import annotations

from .utils import ANSI, _doSysExec


def taskInstall(kwargs: list[str]) -> None:
	"""Run the install task.

	Args:
		kwargs (list[str]): additional args
	"""
	_ = kwargs  # unused - silence pylint
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CB']}Installing{ANSI['CLR']}")
	_doSysExec("poetry install")
	print("Done!")
