"""Übersetzt deutschen Quelltext token-für-token in echtes Python.

Es werden ausschließlich NAME-Token ersetzt, die exakt einem deutschen
Schlüsselwort entsprechen und nicht unmittelbar auf einen Punkt folgen
(Attributzugriffe wie ``objekt.methode`` bleiben also unverändert). Strings,
Kommentare und Zahlen werden nie verändert. Dadurch bleibt jede
Fremdbibliothek (die weiterhin auf Englisch angesprochen wird) uneingeschränkt
nutzbar.
"""

from __future__ import annotations

import io
import token as _token
import tokenize

from .keywords import DEUTSCH_ZU_PYTHON

_IGNORIERTE_TYPEN = frozenset(
    {
        tokenize.NL,
        tokenize.NEWLINE,
        tokenize.COMMENT,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.ENCODING,
    }
)


class DeutscherSyntaxfehler(SyntaxError):
    """Wird ausgelöst, wenn deutscher Quelltext nicht tokenisiert werden kann."""


def uebersetze_quelltext(quelltext: str) -> str:
    """Gibt den quelltext mit deutschen Schlüsselwörtern als echtes Python zurück."""
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(quelltext).readline))
    except tokenize.TokenError as fehler:
        raise DeutscherSyntaxfehler(str(fehler)) from fehler

    ergebnis: list[tokenize.TokenInfo] = []
    letztes_relevantes_token: str | None = None

    for tok in tokens:
        wert = tok.string
        if (
            tok.type == _token.NAME
            and letztes_relevantes_token != "."
            and wert in DEUTSCH_ZU_PYTHON
        ):
            wert = DEUTSCH_ZU_PYTHON[wert]

        ergebnis.append(tok._replace(string=wert))

        if tok.type not in _IGNORIERTE_TYPEN:
            letztes_relevantes_token = tok.string

    return tokenize.untokenize(ergebnis)


def uebersetze_datei(pfad: str, *, kodierung: str = "utf-8") -> str:
    with open(pfad, encoding=kodierung) as datei:
        return uebersetze_quelltext(datei.read())
