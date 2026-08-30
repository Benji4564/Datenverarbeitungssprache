"""Lateinischer Wrapper für das Modul ``time``."""

from __future__ import annotations

import time as _time

nunc = _time.time
dormi = _time.sleep
tempus_locale = _time.localtime
formata = _time.strftime
