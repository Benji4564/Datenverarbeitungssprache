"""Deutscher Wrapper für das Modul ``csv``.

Heißt bewusst weiterhin ``csv`` (Dateiformat-Name), nur die Funktionen und
Klassen bekommen deutsche Namen.
"""

from __future__ import annotations

import csv as _csv

leser = _csv.reader
schreiber = _csv.writer
Wörterbuchleser = _csv.DictReader
Wörterbuchschreiber = _csv.DictWriter
