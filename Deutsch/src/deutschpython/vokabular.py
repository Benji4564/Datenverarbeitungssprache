"""Optionales Vokabular: deutsche Namen für die gängigsten eingebauten Funktionen.

Anders als die Schlüsselwörter (siehe ``keywords.py``) werden diese Namen
NICHT automatisch vom Transpiler ersetzt, weil das echte Bezeichner aus
Fremdbibliotheken zerstören könnte (z. B. einen Funktionsparameter namens
``typ``). Stattdessen sind es ganz normale Python-Zuweisungen, die man sich
per ``importiere vokabular`` in eine ``.dpy``-Datei holen kann::

    importiere vokabular
    drucke(vokabular.länge([1, 2, 3]))

oder gezielt einzelne Namen::

    von vokabular importiere drucke, bereich
"""

from __future__ import annotations

drucke = print
länge = len
bereich = range
eingabe = input
zeichenkette = str
ganzzahl = int
gleitkommazahl = float
liste = list
wörterbuch = dict
tupel = tuple
menge = set
öffne = open
typ = type
größte = max
kleinste = min
summe = sum
sortiert = sorted
aufzählen = enumerate
verbinde = zip
