"""Deutscher Wrapper für das Modul ``os.path``."""

from __future__ import annotations

import os.path as _pfad

existiert = _pfad.exists
verbinde = _pfad.join
basisname = _pfad.basename
verzeichnisname = _pfad.dirname
absoluter_pfad = _pfad.abspath
ist_datei = _pfad.isfile
ist_verzeichnis = _pfad.isdir
teile = _pfad.split
teile_endung = _pfad.splitext
