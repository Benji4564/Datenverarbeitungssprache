"""Import-Hook, damit ``importiere meinmodul`` auch ``.dpy``-Dateien findet.

Die Installation fügt den Standard-Importmechanismen von Python einen
zusätzlichen Loader für die Dateiendung ``.dpy`` hinzu (genau wie z. B.
Cython das für ``.pyx`` macht). Normale ``.py``-Dateien und alle
installierten Pakete funktionieren unverändert weiter – das Deutsch-Python
ist also zu 100 % mit dem restlichen Python-Ökosystem kompatibel.
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import sys

from .transpiler import uebersetze_quelltext

DATEIENDUNG = ".dpy"

_installiert = False


class DeutschQuellcodeLoader(importlib.machinery.SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize=-1):  # type: ignore[override]
        quelltext = importlib.util.decode_source(data)
        uebersetzt = uebersetze_quelltext(quelltext)
        return compile(uebersetzt, path, "exec", dont_inherit=True, optimize=_optimize)


def installiere() -> None:
    """Registriert den Deutsch-Loader in sys.path_hooks (einmalig, idempotent)."""
    global _installiert
    if _installiert:
        return

    # FileFinder.path_hook baut einen Verzeichnis-Importer, der NUR die ihm
    # übergebenen Loader kennt. Würden wir nur unseren .dpy-Loader angeben,
    # würde dieser neue Hook (an Position 0) für JEDES Verzeichnis auf
    # sys.path zuständig und dabei die normalen .py-/.pyc-/Erweiterungs-
    # Loader verdecken. Deshalb kombinieren wir unseren Loader mit den
    # Standard-Loadern zu einem einzigen FileFinder-Hook.
    loader_details = [
        (importlib.machinery.ExtensionFileLoader, importlib.machinery.EXTENSION_SUFFIXES),
        (DeutschQuellcodeLoader, [DATEIENDUNG]),
        (importlib.machinery.SourceFileLoader, importlib.machinery.SOURCE_SUFFIXES),
        (importlib.machinery.SourcelessFileLoader, importlib.machinery.BYTECODE_SUFFIXES),
    ]
    hook = importlib.machinery.FileFinder.path_hook(*loader_details)
    sys.path_hooks.insert(0, hook)
    # Nur den eigenen Cache leeren, damit bereits durchsuchte Verzeichnisse den
    # neuen Loader mit aufnehmen. importlib.invalidate_caches() würde auch
    # fremde, ggf. inkompatible Meta-Path-Finder anfassen, die hier nichts
    # mit unserem Import-Hook zu tun haben.
    sys.path_importer_cache.clear()
    _installiert = True
