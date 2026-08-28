"""Kommandozeilenwerkzeug: ``dpy datei.dpy [Argumente...]`` führt eine deutsche
Python-Datei normal aus (auch wenn sie andere .dpy- oder .py-Module importiert)."""

from __future__ import annotations

import sys

from .loader import installiere
from .transpiler import DeutscherSyntaxfehler, uebersetze_quelltext


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("Nutzung: dpy <datei.dpy> [Argumente für das Skript...]", file=sys.stderr)
        return 2

    pfad = argv[0]
    installiere()  # damit weitere "importiere ..."-Anweisungen .dpy-Module finden

    try:
        with open(pfad, encoding="utf-8") as datei:
            quelltext = datei.read()
        uebersetzt = uebersetze_quelltext(quelltext)
        code = compile(uebersetzt, pfad, "exec")
    except DeutscherSyntaxfehler as fehler:
        print(f"Syntaxfehler beim Übersetzen von {pfad}: {fehler}", file=sys.stderr)
        return 1
    except OSError as fehler:
        print(f"Konnte {pfad} nicht lesen: {fehler}", file=sys.stderr)
        return 1

    sys.argv = list(argv)
    namensraum = {"__name__": "__main__", "__file__": pfad}
    exec(code, namensraum)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
