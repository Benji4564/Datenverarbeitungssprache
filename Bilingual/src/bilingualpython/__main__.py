"""Generischer CLI-Kern: ``python -m bilingualpython <sprache> datei [Argumente...]``
führt eine fremdsprachige Python-Datei normal aus. Die eigentlichen
Befehle ``dpy`` (Deutsch) und ``lpy`` (Latein) sind dünne Wrapper darum,
siehe ``pyproject.toml``."""

from __future__ import annotations

import sys

from .keywords import SPRACHEN
from .loader import installiere
from .transpiler import SyntaxfehlerInFremdsprache, uebersetze_quelltext


def fuehre_aus(sprache: str, argv: list[str]) -> int:
    if not argv:
        eintrag = SPRACHEN[sprache]
        endung = eintrag["dateiendung"]
        print(f"Nutzung: <befehl> <datei{endung}> [Argumente für das Skript...]", file=sys.stderr)
        return 2

    pfad = argv[0]
    installiere()  # damit weitere Import-Anweisungen fremdsprachige Module finden

    try:
        with open(pfad, encoding="utf-8") as datei:
            quelltext = datei.read()
        uebersetzt = uebersetze_quelltext(quelltext, sprache)
        code = compile(uebersetzt, pfad, "exec")
    except SyntaxfehlerInFremdsprache as fehler:
        print(f"Syntaxfehler beim Übersetzen von {pfad}: {fehler}", file=sys.stderr)
        return 1
    except OSError as fehler:
        print(f"Konnte {pfad} nicht lesen: {fehler}", file=sys.stderr)
        return 1

    sys.argv = list(argv)
    namensraum = {"__name__": "__main__", "__file__": pfad}
    exec(code, namensraum)
    return 0


def main(argv: list[str] | None = None) -> int:
    """Aufruf als ``python -m bilingualpython <sprache> datei.ext``."""
    argv = sys.argv[1:] if argv is None else argv
    if not argv or argv[0] not in SPRACHEN:
        gueltig = ", ".join(sorted(SPRACHEN))
        print(f"Nutzung: python -m bilingualpython <sprache> <datei> ...", file=sys.stderr)
        print(f"Bekannte Sprachen: {gueltig}", file=sys.stderr)
        return 2
    return fuehre_aus(argv[0], argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
