"""Lateinischer Wrapper für das Modul ``os.path`` (semita = der Pfad, Weg)."""

from __future__ import annotations

import os.path as _semita

existit = _semita.exists
iunge = _semita.join
nomen_basis = _semita.basename
nomen_directorii = _semita.dirname
semita_absoluta = _semita.abspath
est_charta = _semita.isfile
est_directorium = _semita.isdir
divide = _semita.split
