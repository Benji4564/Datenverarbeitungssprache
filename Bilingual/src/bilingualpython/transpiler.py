"""Übersetzt Quelltext einer unterstützten Sprache token-für-token in echtes Python.

Es werden ausschließlich NAME-Token ersetzt, die exakt einem
Schlüsselwort der gewählten Sprache entsprechen und nicht unmittelbar auf
einen Punkt folgen (Attributzugriffe wie ``objekt.methode`` bleiben also
unverändert). Strings, Kommentare und Zahlen werden nie verändert. Dadurch
bleibt jede Fremdbibliothek (die weiterhin auf Englisch angesprochen wird)
uneingeschränkt nutzbar.
"""

from __future__ import annotations

import io
import token as _token
import tokenize

from .keywords import SPRACHEN

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


class SyntaxfehlerInFremdsprache(SyntaxError):
    """Wird ausgelöst, wenn der Quelltext einer Sprache nicht tokenisiert werden kann."""


def _schluesselwoerter(sprache: str) -> dict[str, str]:
    try:
        eintrag = SPRACHEN[sprache]
    except KeyError as fehler:
        gueltig = ", ".join(sorted(SPRACHEN))
        raise ValueError(f"Unbekannte Sprache {sprache!r}. Bekannt: {gueltig}") from fehler
    return eintrag["schluesselwoerter"]  # type: ignore[return-value]


def uebersetze_quelltext(quelltext: str, sprache: str = "deutsch") -> str:
    """Gibt den Quelltext der gewählten Sprache als echtes Python zurück."""
    woerterbuch = _schluesselwoerter(sprache)

    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(quelltext).readline))
    except tokenize.TokenError as fehler:
        raise SyntaxfehlerInFremdsprache(str(fehler)) from fehler

    ergebnis: list[tokenize.TokenInfo] = []
    letztes_relevantes_token: str | None = None

    for tok in tokens:
        wert = tok.string
        if (
            tok.type == _token.NAME
            and letztes_relevantes_token != "."
            and wert in woerterbuch
        ):
            wert = woerterbuch[wert]

        ergebnis.append(tok._replace(string=wert))

        if tok.type not in _IGNORIERTE_TYPEN:
            letztes_relevantes_token = tok.string

    return tokenize.untokenize(ergebnis)


def uebersetze_datei(pfad: str, sprache: str = "deutsch", *, kodierung: str = "utf-8") -> str:
    with open(pfad, encoding=kodierung) as datei:
        return uebersetze_quelltext(datei.read(), sprache)


def sprache_zu_dateiendung(sprache: str) -> str:
    return _sprache_feld(sprache, "dateiendung")


def dateiendung_zu_sprache(dateiendung: str) -> str | None:
    for sprache, eintrag in SPRACHEN.items():
        if eintrag["dateiendung"] == dateiendung:
            return sprache
    return None


def _sprache_feld(sprache: str, feld: str):
    try:
        return SPRACHEN[sprache][feld]
    except KeyError as fehler:
        gueltig = ", ".join(sorted(SPRACHEN))
        raise ValueError(f"Unbekannte Sprache {sprache!r}. Bekannt: {gueltig}") from fehler
