"""Deutscher Wrapper für das Modul ``json``.

Heißt bewusst weiterhin ``json`` (Dateiformat-Name, kein deutsches Wort),
nur die Funktionen bekommen deutsche Namen.
"""

from __future__ import annotations

import json as _json

lade = _json.load
lade_zeichenkette = _json.loads
speichere = _json.dump
speichere_als_zeichenkette = _json.dumps
