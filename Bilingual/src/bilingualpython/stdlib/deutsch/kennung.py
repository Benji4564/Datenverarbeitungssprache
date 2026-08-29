"""Deutscher Wrapper für das Modul ``uuid``."""

from __future__ import annotations

import uuid as _uuid

ID = _uuid.UUID
zufalls_id = _uuid.uuid4
namensbasierte_id = _uuid.uuid5
