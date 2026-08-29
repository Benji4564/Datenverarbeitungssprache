"""Deutscher Wrapper für das Modul ``threading``."""

from __future__ import annotations

import threading as _threading

Faden = _threading.Thread
Sperre = _threading.Lock
Ereignis = _threading.Event
aktueller_faden = _threading.current_thread
