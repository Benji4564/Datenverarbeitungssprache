import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import math
import os

from bilingualpython.stdlib.deutsch import (  # noqa: E402
    betriebssystem,
    datum,
    funktional,
    json,
    mathematik,
    pfad,
    sammlungen,
    statistik,
    system,
    text,
    zeit,
    zufall,
)


def test_mathematik():
    assert mathematik.pi == math.pi
    assert mathematik.wurzel(9) == 3.0
    assert mathematik.aufrunden(1.2) == 2
    assert mathematik.fakultät(5) == 120


def test_zufall():
    zufall.setze_startwert(42)
    wert = zufall.ganzzahl(1, 10)
    assert 1 <= wert <= 10


def test_zeit():
    assert zeit.jetzt() > 0


def test_datum():
    heute = datum.heute()
    assert isinstance(heute, datum.Datum)
    zeitstempel = datum.jetzt()
    assert isinstance(zeitstempel, datum.Zeitstempel)


def test_betriebssystem_und_pfad():
    assert betriebssystem.aktuelles_verzeichnis() == os.getcwd()
    assert pfad.existiert(__file__)
    assert pfad.basisname("/a/b/c.txt") == "c.txt"


def test_system():
    assert system.plattform == sys.platform


def test_json():
    daten = {"a": 1, "b": [1, 2, 3]}
    text_ = json.speichere_als_zeichenkette(daten)
    assert json.lade_zeichenkette(text_) == daten


def test_sammlungen():
    zaehler = sammlungen.Zähler("aabbbc")
    assert zaehler["b"] == 3
    schlange = sammlungen.Schlange([1, 2, 3])
    schlange.appendleft(0)
    assert list(schlange) == [0, 1, 2, 3]


def test_statistik():
    assert statistik.mittelwert([1, 2, 3, 4]) == 2.5
    assert statistik.median([1, 2, 3]) == 2


def test_text():
    assert text.finde_alle(r"\d+", "a1 b22 c333") == ["1", "22", "333"]
    assert text.ersetze(r"\s+", "_", "a b  c") == "a_b_c"


def test_funktional():
    assert funktional.reduziere(lambda a, b: a + b, [1, 2, 3, 4]) == 10
    assert list(funktional.kombinationen([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]
