"""Deutscher Wrapper für das Modul ``time``."""

from __future__ import annotations

import time as _time

jetzt = _time.time
schlafe = _time.sleep
lokale_zeit = _time.localtime
weltzeit = _time.gmtime
formatiere = _time.strftime
verarbeite = _time.strptime
monotone_zeit = _time.monotonic
leistungszähler = _time.perf_counter
