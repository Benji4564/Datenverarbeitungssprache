"""Deutscher Wrapper für das Modul ``os`` (ohne ``os.path``, siehe ``pfad``)."""

from __future__ import annotations

import os as _os

umgebung = _os.environ
aktuelles_verzeichnis = _os.getcwd
wechsle_verzeichnis = _os.chdir
verzeichnis_auflisten = _os.listdir
erstelle_verzeichnis = _os.mkdir
erstelle_verzeichnisse = _os.makedirs
lösche_datei = _os.remove
lösche_verzeichnis = _os.rmdir
benenne_um = _os.rename
trennzeichen = _os.sep
zeilenumbruch = _os.linesep
