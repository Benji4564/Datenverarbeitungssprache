"""Lateinischer Wrapper für das Modul ``os`` (ohne ``os.path``, siehe ``semita``)."""

from __future__ import annotations

import os as _os

ambitus = _os.environ
directorium_actuale = _os.getcwd
muta_directorium = _os.chdir
enumera_directorium = _os.listdir
crea_directorium = _os.mkdir
crea_directoria = _os.makedirs
dele_rem = _os.remove
dele_directorium = _os.rmdir
renomina = _os.rename
separator = _os.sep
