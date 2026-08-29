"""Deutscher Wrapper für das Modul ``pathlib`` (objektorientierte Pfade).

Heißt bewusst nicht ``pfad`` – dieser Name ist bereits für den
``os.path``-Wrapper vergeben (siehe ``pfad.py``).
"""

from __future__ import annotations

import pathlib as _pathlib

Pfad = _pathlib.Path
PurerPfad = _pathlib.PurePath

heimatverzeichnis = _pathlib.Path.home
aktuelles_verzeichnis = _pathlib.Path.cwd
