"""Zuordnung der reservierten Python-Wörter je unterstützter Sprache.

Nur die reservierten Wörter von Python werden übersetzt. Bezeichner aus
importierten Paketen (z. B. ``os.path``) bleiben unangetastet, weil der
Transpiler nur ganze NAME-Token ersetzt, die exakt einem Eintrag hier
entsprechen, und niemals ein Token direkt nach einem Punkt (Attributzugriff).

Um eine neue Sprache hinzuzufügen: ein neues ``dict`` (Sprachwort ->
echtes Python-Schlüsselwort) anlegen und in ``SPRACHEN`` unter einem
Sprachcode mit Dateiendung eintragen.
"""

from __future__ import annotations

# Deutsch --------------------------------------------------------------
# "in", "lambda" und "global" existieren unverändert auch im Deutschen und
# werden daher nicht extra aufgeführt.
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

# Latein -----------------------------------------------------------------
# "in" und "lambda" bleiben unverändert (im Lateinischen ist "in" ohnehin
# dieselbe Präposition). "global" wird ebenfalls nicht übersetzt.
#
# Viele Wörter sind bewusst echtes klassisches Latein: si (wenn), dum
# (während), cum (mit), non (nicht), vel (oder), est (ist), ex (von),
# pro (für). Für Sprachelemente ohne antikes Vorbild (def, class, ...)
# wurden lateinische Verben/Nomen mit passender Bedeutung gewählt, im
# Imperativ, so wie das Deutsche z. B. "gib_zurück" für return nutzt.
LATEIN_ZU_PYTHON: dict[str, str] = {
    "Falsum": "False",
    "Nihil": "None",
    "Verum": "True",
    "et": "and",
    "ut": "as",
    "assere": "assert",
    "simul": "async",
    "exspecta": "await",
    "rumpe": "break",
    "classis": "class",
    "perge": "continue",
    "functio": "def",
    "dele": "del",
    "alitersi": "elif",
    "aliter": "else",
    "excipe": "except",
    "denique": "finally",
    "pro": "for",
    "ex": "from",
    "si": "if",
    "importa": "import",
    "est": "is",
    "exterius": "nonlocal",
    "non": "not",
    "vel": "or",
    "transi": "pass",
    "iace": "raise",
    "redde": "return",
    "tenta": "try",
    "dum": "while",
    "cum": "with",
    "cede": "yield",
}

# Registry: Sprachcode -> (Schlüsselwörter, Dateiendung, Anzeigename)
SPRACHEN: dict[str, dict[str, object]] = {
    "deutsch": {
        "schluesselwoerter": DEUTSCH_ZU_PYTHON,
        "dateiendung": ".dpy",
        "anzeigename": "Deutsch-Python",
    },
    "latein": {
        "schluesselwoerter": LATEIN_ZU_PYTHON,
        "dateiendung": ".lpy",
        "anzeigename": "Latein-Python (Lingua Latina Python)",
    },
}

# Umkehrabbildungen, z. B. um übersetzten Quelltext aus englischem zu erzeugen.
PYTHON_ZU_DEUTSCH: dict[str, str] = {v: k for k, v in DEUTSCH_ZU_PYTHON.items()}
PYTHON_ZU_LATEIN: dict[str, str] = {v: k for k, v in LATEIN_ZU_PYTHON.items()}
