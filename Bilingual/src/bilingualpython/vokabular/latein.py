"""Optionales Vokabular: lateinische Namen für die gängigsten eingebauten Funktionen.

Anders als die Schlüsselwörter (siehe ``keywords.py``) werden diese Namen
NICHT automatisch vom Transpiler ersetzt. Stattdessen sind es ganz normale
Python-Zuweisungen, die man sich in eine ``.lpy``-Datei holen kann::

    importa bilingualpython.vokabular.latein ut vocabularium
    scribe(vocabularium.longitudo([1, 2, 3]))

oder gezielt einzelne Namen::

    ex bilingualpython.vokabular.latein importa scribe, intervallum

Viele Namen sind bewusst echte, klassische lateinische Wörter (``summa``,
``maximum``, ``minimum``, ``integer``, ``genus`` sind sogar die
etymologischen Ursprünge der gleichnamigen englischen Fachbegriffe).
"""

from __future__ import annotations

scribe = print
longitudo = len
intervallum = range
posce = input
catena = str
integer = int
fractio = float
album = list
lexicon = dict
fasciculus = tuple
copia = set
aperi = open
genus = type
maximum = max
minimum = min
summa = sum
ordinata = sorted
enumera = enumerate
iunge = zip
