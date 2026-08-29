"""Deutscher Wrapper für das Modul ``subprocess``."""

from __future__ import annotations

import subprocess as _subprocess

starte = _subprocess.run
öffne_prozess = _subprocess.Popen
Prozessfehler = _subprocess.CalledProcessError
Zeitüberschreitung = _subprocess.TimeoutExpired
UMLEITUNG = _subprocess.PIPE
