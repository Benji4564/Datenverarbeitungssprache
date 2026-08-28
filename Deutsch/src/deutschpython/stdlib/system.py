"""Deutscher Wrapper für das Modul ``sys``."""

from __future__ import annotations

import sys as _sys

argumente = _sys.argv
suchpfad = _sys.path
plattform = _sys.platform
standard_ausgabe = _sys.stdout
standard_eingabe = _sys.stdin
standard_fehler = _sys.stderr
version = _sys.version
beenden = _sys.exit
