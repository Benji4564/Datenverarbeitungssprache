"""Lateinischer Wrapper für das Modul ``re`` (reguläre Ausdrücke)."""

from __future__ import annotations

import re as _re

quaere = _re.search
convenit = _re.match
convenit_totum = _re.fullmatch
inveni_omnia = _re.findall
substitue = _re.sub
divide = _re.split
compone = _re.compile
