import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from bilingualpython.transpiler import uebersetze_quelltext  # noqa: E402

BEISPIELE = Path(__file__).resolve().parents[1] / "beispiele"
SRC = Path(__file__).resolve().parents[1] / "src"


def test_einfache_uebersetzung_deutsch():
    quelltext = "wenn Wahr:\n    drucke = 1\n"
    ergebnis = uebersetze_quelltext(quelltext, "deutsch")
    assert ergebnis.splitlines()[0].strip() == "if True:"


def test_einfache_uebersetzung_latein():
    quelltext = "si Verum:\n    scribe = 1\n"
    ergebnis = uebersetze_quelltext(quelltext, "latein")
    assert ergebnis.splitlines()[0].strip() == "if True:"


def test_string_und_kommentar_bleiben_unveraendert():
    quelltext = 'x = "wenn das ein Text ist"  # wenn das ein Kommentar ist\n'
    ergebnis = uebersetze_quelltext(quelltext, "deutsch")
    assert 'x = "wenn das ein Text ist"' in ergebnis
    assert "# wenn das ein Kommentar ist" in ergebnis


def test_attributzugriff_bleibt_unveraendert():
    quelltext = "objekt.klasse\n"
    ergebnis = uebersetze_quelltext(quelltext, "deutsch")
    assert ergebnis.strip() == "objekt.klasse"

    quelltext_latein = "objectum.classis\n"
    ergebnis_latein = uebersetze_quelltext(quelltext_latein, "latein")
    assert ergebnis_latein.strip() == "objectum.classis"


def test_unbekannte_sprache_wirft_fehler():
    try:
        uebersetze_quelltext("wenn Wahr: weiter\n", "griechisch")
    except ValueError as fehler:
        assert "griechisch" in str(fehler)
    else:
        raise AssertionError("ValueError wurde nicht ausgelöst")


def test_uebersetzter_quelltext_ist_gueltiges_python_deutsch():
    quelltext = (
        "klasse Zähler:\n"
        "    funktion __init__(selbst):\n"
        "        selbst.wert = 0\n"
        "\n"
        "    funktion erhöhen(selbst):\n"
        "        selbst.wert = selbst.wert + 1\n"
        "        gib_zurück selbst.wert\n"
    )
    uebersetzt = uebersetze_quelltext(quelltext, "deutsch")
    namensraum: dict = {}
    exec(compile(uebersetzt, "<test>", "exec"), namensraum)
    zaehler = namensraum["Zähler"]()
    assert zaehler.erhöhen() == 1
    assert zaehler.erhöhen() == 2


def test_uebersetzter_quelltext_ist_gueltiges_python_latein():
    quelltext = (
        "classis Numerator:\n"
        "    functio __init__(se):\n"
        "        se.valor = 0\n"
        "\n"
        "    functio incrementa(se):\n"
        "        se.valor = se.valor + 1\n"
        "        redde se.valor\n"
    )
    uebersetzt = uebersetze_quelltext(quelltext, "latein")
    namensraum: dict = {}
    exec(compile(uebersetzt, "<test>", "exec"), namensraum)
    numerator = namensraum["Numerator"]()
    assert numerator.incrementa() == 1
    assert numerator.incrementa() == 2


def test_beispieldatei_hallo_welt_laeuft_ueber_cli():
    skript = BEISPIELE / "hallo_welt.dpy"
    ergebnis = subprocess.run(
        [sys.executable, "-m", "bilingualpython", "deutsch", str(skript)],
        cwd=SRC,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert ergebnis.returncode == 0, ergebnis.stderr
    assert "Hallo, Welt!" in ergebnis.stdout
    assert "5! = 120" in ergebnis.stdout
    assert "Fehler abgefangen: n muss >= 0 sein" in ergebnis.stdout


def test_beispieldatei_fibonacci_laeuft_ueber_cli():
    skript = BEISPIELE / "fibonacci.dpy"
    ergebnis = subprocess.run(
        [sys.executable, "-m", "bilingualpython", "deutsch", str(skript)],
        cwd=SRC,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert ergebnis.returncode == 0, ergebnis.stderr
    assert ergebnis.stdout.strip() == "0 1 1 2 3 5 8 13 21 34"


def test_beispieldatei_salve_mundi_laeuft_ueber_cli():
    skript = BEISPIELE / "latein" / "salve_mundi.lpy"
    ergebnis = subprocess.run(
        [sys.executable, "-m", "bilingualpython", "latein", str(skript)],
        cwd=SRC,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert ergebnis.returncode == 0, ergebnis.stderr
    assert "Salve, Mundus!" in ergebnis.stdout
    assert "5! = 120" in ergebnis.stdout
    assert "Error captus: n debet >= 0 esse" in ergebnis.stdout
