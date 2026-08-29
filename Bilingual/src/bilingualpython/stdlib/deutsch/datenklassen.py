"""Deutscher Wrapper für das Modul ``dataclasses``."""

from __future__ import annotations

import dataclasses as _dataclasses

datenklasse = _dataclasses.dataclass
feld = _dataclasses.field
ist_datenklasse = _dataclasses.is_dataclass
zu_wörterbuch = _dataclasses.asdict
