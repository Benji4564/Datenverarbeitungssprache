"""deutschpython: Python mit deutschen Schlüsselwörtern, kompatibel mit jedem Paket.

Kernfunktionen:
    uebersetze_quelltext(text) -> str   Übersetzt deutschen Quelltext nach Python.
    installiere()                       Registriert den Import-Hook für .dpy-Dateien.
"""

from .loader import installiere
from .transpiler import DeutscherSyntaxfehler, uebersetze_datei, uebersetze_quelltext

__all__ = [
    "DeutscherSyntaxfehler",
    "installiere",
    "uebersetze_datei",
    "uebersetze_quelltext",
]

__version__ = "0.1.0"
