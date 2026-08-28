"""Zuordnung von deutschen Schlüsselwörtern zu den echten Python-Schlüsselwörtern.

Nur die 33 reservierten Wörter von Python werden übersetzt. Bezeichner aus
importierten Paketen (z. B. ``os.path``) bleiben unangetastet, weil der
Transpiler nur ganze NAME-Token ersetzt, die exakt einem Eintrag hier
entsprechen, und niemals ein Token direkt nach einem Punkt (Attributzugriff).

"in", "lambda" und "global" existieren unverändert auch im Deutschen und
werden daher nicht extra aufgeführt.
"""

from __future__ import annotations

DEUTSCH_ZU_PYTHON: dict[str, str] = {
    "Falsch": "False",
    "Nichts": "None",
    "Wahr": "True",
    "und": "and",
    "als": "as",
    "versichere": "assert",
    "asynchron": "async",
    "erwarte": "await",
    "abbrechen": "break",
    "klasse": "class",
    "weitermachen": "continue",
    "funktion": "def",
    "lösche": "del",
    "sonstwenn": "elif",
    "sonst": "else",
    "außer": "except",
    "schließlich": "finally",
    "für": "for",
    "von": "from",
    "wenn": "if",
    "importiere": "import",
    "ist": "is",
    "nichtlokal": "nonlocal",
    "nicht": "not",
    "oder": "or",
    "weiter": "pass",
    "werfe": "raise",
    "gib_zurück": "return",
    "versuche": "try",
    "während": "while",
    "mit": "with",
    "liefere": "yield",
}

# Umkehrabbildung, z. B. um deutschen Quelltext aus englischem zu erzeugen.
PYTHON_ZU_DEUTSCH: dict[str, str] = {v: k for k, v in DEUTSCH_ZU_PYTHON.items()}
