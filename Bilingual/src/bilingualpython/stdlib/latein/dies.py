"""Lateinischer Wrapper für das Modul ``datetime`` (dies = der Tag)."""

from __future__ import annotations

import datetime as _datetime

Dies = _datetime.date
Hora = _datetime.time
Momentum = _datetime.datetime
Intervallum = _datetime.timedelta

hodie = _datetime.date.today
nunc = _datetime.datetime.now
