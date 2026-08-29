"""Import-Hook, damit ``importiere``/``importa``/... auch fremdsprachige Dateien findet.

Für jede in ``keywords.SPRACHEN`` registrierte Sprache wird ein Loader für
ihre Dateiendung installiert (``.dpy`` für Deutsch, ``.lpy`` für Latein,
...) – genau wie z. B. Cython das für ``.pyx`` macht. Normale ``.py``-
Dateien und alle installierten Pakete funktionieren unverändert weiter –
das bilinguale Python ist also zu 100 % mit dem restlichen
Python-Ökosystem kompatibel.
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import sys

from .keywords import SPRACHEN
from .transpiler import uebersetze_quelltext

_installiert = False


def _mache_loader(sprache: str) -> type[importlib.machinery.SourceFileLoader]:
    class _SprachLoader(importlib.machinery.SourceFileLoader):
        def source_to_code(self, data, path, *, _optimize=-1):  # type: ignore[override]
            quelltext = importlib.util.decode_source(data)
            uebersetzt = uebersetze_quelltext(quelltext, sprache)
            return compile(uebersetzt, path, "exec", dont_inherit=True, optimize=_optimize)

    _SprachLoader.__name__ = f"{sprache.capitalize()}QuellcodeLoader"
    _SprachLoader.__qualname__ = _SprachLoader.__name__
    return _SprachLoader


def installiere() -> None:
    """Registriert die Import-Hooks für alle Sprachen (einmalig, idempotent)."""
    global _installiert
    if _installiert:
        return

    # FileFinder.path_hook baut einen Verzeichnis-Importer, der NUR die ihm
    # übergebenen Loader kennt. Würden wir nur unsere Sprach-Loader angeben,
    # würde dieser neue Hook (an Position 0) für JEDES Verzeichnis auf
    # sys.path zuständig und dabei die normalen .py-/.pyc-/Erweiterungs-
    # Loader verdecken. Deshalb kombinieren wir unsere Loader mit den
    # Standard-Loadern zu einem einzigen FileFinder-Hook.
    loader_details = [
        (importlib.machinery.ExtensionFileLoader, importlib.machinery.EXTENSION_SUFFIXES),
    ]
    for sprache, eintrag in SPRACHEN.items():
        loader_details.append((_mache_loader(sprache), [eintrag["dateiendung"]]))
    loader_details.append(
        (importlib.machinery.SourceFileLoader, importlib.machinery.SOURCE_SUFFIXES)
    )
    loader_details.append(
        (importlib.machinery.SourcelessFileLoader, importlib.machinery.BYTECODE_SUFFIXES)
    )

    hook = importlib.machinery.FileFinder.path_hook(*loader_details)
    sys.path_hooks.insert(0, hook)
    # Nur den eigenen Cache leeren, damit bereits durchsuchte Verzeichnisse den
    # neuen Loader mit aufnehmen. importlib.invalidate_caches() würde auch
    # fremde, ggf. inkompatible Meta-Path-Finder anfassen, die hier nichts
    # mit unserem Import-Hook zu tun haben.
    sys.path_importer_cache.clear()
    _installiert = True
