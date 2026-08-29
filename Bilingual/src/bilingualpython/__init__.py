"""bilingualpython: Python mit fremdsprachigen Schlüsselwörtern, kompatibel mit jedem Paket.

Unterstützte Sprachen (siehe ``keywords.SPRACHEN``): Deutsch (``.dpy``),
Latein (``.lpy``).

Kernfunktionen:
    uebersetze_quelltext(text, sprache) -> str   Übersetzt Quelltext nach Python.
    installiere()                                Registriert die Import-Hooks.
"""

from .keywords import SPRACHEN
from .loader import installiere
from .transpiler import SyntaxfehlerInFremdsprache, uebersetze_datei, uebersetze_quelltext

__all__ = [
    "SPRACHEN",
    "SyntaxfehlerInFremdsprache",
    "installiere",
    "uebersetze_datei",
    "uebersetze_quelltext",
]

__version__ = "0.1.0"
