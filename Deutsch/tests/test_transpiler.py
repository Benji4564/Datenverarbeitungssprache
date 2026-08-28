import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from deutschpython.transpiler import uebersetze_quelltext  # noqa: E402

BEISPIELE = Path(__file__).resolve().parents[1] / "beispiele"


def test_einfache_uebersetzung():
    quelltext = "wenn Wahr:\n    drucke = 1\n"
    ergebnis = uebersetze_quelltext(quelltext)
    assert ergebnis.splitlines()[0].strip() == "if True:"


def test_string_und_kommentar_bleiben_unveraendert():
    quelltext = 'x = "wenn das ein Text ist"  # wenn das ein Kommentar ist\n'
    ergebnis = uebersetze_quelltext(quelltext)
    assert 'x = "wenn das ein Text ist"' in ergebnis
    assert "# wenn das ein Kommentar ist" in ergebnis


def test_attributzugriff_bleibt_unveraendert():
    quelltext = "objekt.klasse\n"
    ergebnis = uebersetze_quelltext(quelltext)
    assert ergebnis.strip() == "objekt.klasse"


def test_uebersetzter_quelltext_ist_gueltiges_python():
    quelltext = (
        "klasse Zähler:\n"
        "    funktion __init__(selbst):\n"
        "        selbst.wert = 0\n"
        "\n"
        "    funktion erhöhen(selbst):\n"
        "        selbst.wert = selbst.wert + 1\n"
        "        gib_zurück selbst.wert\n"
    )
    uebersetzt = uebersetze_quelltext(quelltext)
    namensraum: dict = {}
    exec(compile(uebersetzt, "<test>", "exec"), namensraum)
    zaehler = namensraum["Zähler"]()
    assert zaehler.erhöhen() == 1
    assert zaehler.erhöhen() == 2


def test_beispieldatei_hallo_welt_laeuft_ueber_cli():
    skript = BEISPIELE / "hallo_welt.dpy"
    ergebnis = subprocess.run(
        [sys.executable, "-m", "deutschpython", str(skript)],
        cwd=Path(__file__).resolve().parents[1] / "src",
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
        [sys.executable, "-m", "deutschpython", str(skript)],
        cwd=Path(__file__).resolve().parents[1] / "src",
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert ergebnis.returncode == 0, ergebnis.stderr
    assert ergebnis.stdout.strip() == "0 1 1 2 3 5 8 13 21 34"
