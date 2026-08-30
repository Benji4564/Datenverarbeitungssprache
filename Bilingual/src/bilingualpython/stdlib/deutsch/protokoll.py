"""Deutscher Wrapper für das Modul ``logging``."""

from __future__ import annotations

import logging as _logging

hole_protokollierer = _logging.getLogger
konfiguriere = _logging.basicConfig

DEBUG = _logging.DEBUG
INFO = _logging.INFO
WARNUNG = _logging.WARNING
FEHLER = _logging.ERROR
KRITISCH = _logging.CRITICAL
