"""Deutscher Wrapper für das Modul ``shutil``."""

from __future__ import annotations

import shutil as _shutil

kopiere = _shutil.copy
kopiere_mit_metadaten = _shutil.copy2
kopiere_baum = _shutil.copytree
verschiebe = _shutil.move
lösche_baum = _shutil.rmtree
festplattennutzung = _shutil.disk_usage
welcher = _shutil.which
