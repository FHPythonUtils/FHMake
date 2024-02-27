"""publish: Run poetry publish (interactive)."""

from __future__ import annotations

import subprocess

from .utils import ANSI


def taskPublish(kwargs: list[str]) -> None:
	"""Run the publish task.

	Args:
	----
		kwargs (list[str]): additional args

	"""
	_ = kwargs  # unused - silence pylint
	print(f"{ANSI['B']}{ANSI['U']}{ANSI['CB']}Publish{ANSI['CLR']}")
	with subprocess.Popen("poetry publish") as process:
		_ = process.wait()
