"""Sprachgebundene CLI-Einstiegspunkte, siehe ``pyproject.toml`` [project.scripts]."""

from __future__ import annotations

import sys

from .__main__ import fuehre_aus


def dpy() -> int:
    """``dpy datei.dpy [Argumente...]`` – führt eine deutsche Python-Datei aus."""
    return fuehre_aus("deutsch", sys.argv[1:])


def lpy() -> int:
    """``lpy datei.lpy [Argumente...]`` – führt eine lateinische Python-Datei aus."""
    return fuehre_aus("latein", sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(dpy())
