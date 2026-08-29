"""Lateinischer Wrapper für das Modul ``json``.

Heißt bewusst weiterhin ``json`` (Dateiformat-Name), nur die Funktionen
bekommen lateinische Namen.
"""

from __future__ import annotations

import json as _json

onera = _json.load
onera_ex_catena = _json.loads
serva = _json.dump
serva_ut_catenam = _json.dumps
