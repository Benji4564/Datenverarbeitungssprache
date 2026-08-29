import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from deutschpython.stdlib import (  # noqa: E402
    argumentanalyse,
    aufzaehlung,
    csv,
    dateiverwaltung,
    datenklassen,
    kennung,
    kopie,
    nebenlaeufigkeit,
    pfadobjekte,
    protokoll,
    prozess,
    pruefsummen,
)


def test_pfadobjekte():
    p = pfadobjekte.Pfad(__file__)
    assert p.name == "test_stdlib_zwei.py"


def test_csv(tmp_path):
    datei = tmp_path / "daten.csv"
    with open(datei, "w", newline="") as f:
        schreiber = csv.schreiber(f)
        schreiber.writerow(["a", "b"])
    with open(datei) as f:
        zeilen = list(csv.leser(f))
    assert zeilen == [["a", "b"]]


def test_dateiverwaltung(tmp_path):
    quelle = tmp_path / "a.txt"
    quelle.write_text("hallo")
    ziel = tmp_path / "b.txt"
    dateiverwaltung.kopiere(quelle, ziel)
    assert ziel.read_text() == "hallo"


def test_prozess():
    ergebnis = prozess.starte(
        [sys.executable, "-c", "print('hallo')"],
        capture_output=True,
        text=True,
    )
    assert ergebnis.stdout.strip() == "hallo"


def test_nebenlaeufigkeit():
    ergebnisse = []
    faden = nebenlaeufigkeit.Faden(target=lambda: ergebnisse.append(1))
    faden.start()
    faden.join()
    assert ergebnisse == [1]


def test_protokoll():
    logger = protokoll.hole_protokollierer("test")
    assert logger.level == 0 or isinstance(logger.level, int)


def test_argumentanalyse():
    parser = argumentanalyse.Argumentparser()
    parser.add_argument("--wert")
    namensraum = parser.parse_args(["--wert", "42"])
    assert namensraum.wert == "42"


def test_pruefsummen():
    assert pruefsummen.sha256(b"hallo").hexdigest() == pruefsummen.neue_prüfsumme(
        "sha256", b"hallo"
    ).hexdigest()


def test_kennung():
    id_ = kennung.zufalls_id()
    assert isinstance(id_, kennung.ID)


def test_aufzaehlung():
    class Farbe(aufzaehlung.Aufzählung):
        ROT = aufzaehlung.automatisch()
        BLAU = aufzaehlung.automatisch()

    assert Farbe.ROT != Farbe.BLAU


def test_datenklassen():
    @datenklassen.datenklasse
    class Punkt:
        x: int
        y: int

    p = Punkt(1, 2)
    assert datenklassen.ist_datenklasse(p)
    assert datenklassen.zu_wörterbuch(p) == {"x": 1, "y": 2}


def test_kopie():
    original = [1, [2, 3]]
    tief = kopie.tiefe_kopie(original)
    tief[1].append(4)
    assert original == [1, [2, 3]]
