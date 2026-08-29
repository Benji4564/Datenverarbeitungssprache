"""Deutscher Wrapper für das Modul ``re`` (reguläre Ausdrücke)."""

from __future__ import annotations

import re as _re

suche = _re.search
passt = _re.match
passt_vollständig = _re.fullmatch
finde_alle = _re.findall
ersetze = _re.sub
teile = _re.split
kompiliere = _re.compile
