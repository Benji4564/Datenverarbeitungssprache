"""Deutscher Wrapper für das Modul ``datetime``."""

from __future__ import annotations

import datetime as _datetime

Datum = _datetime.date
Uhrzeit = _datetime.time
Zeitstempel = _datetime.datetime
Zeitspanne = _datetime.timedelta
Zeitzone = _datetime.timezone

heute = _datetime.date.today
jetzt = _datetime.datetime.now
