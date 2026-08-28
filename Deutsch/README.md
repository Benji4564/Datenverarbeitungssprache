# deutschpython

Python mit deutschen Schlüsselwörtern – **voll kompatibel** mit dem
normalen Python-Ökosystem (pip-Pakete, Standardbibliothek, C-Erweiterungen
usw.), weil kein Fork von CPython gebaut wird. Stattdessen wird
`.dpy`-Quelltext vor der Ausführung token-für-token in echtes Python
übersetzt und ganz normal von deinem installierten CPython kompiliert.

```dpy
importiere math

funktion fakultät(n):
    wenn n < 0:
        werfe ValueError("n muss >= 0 sein")
    ergebnis = 1
    für i in range(2, n + 1):
        ergebnis = ergebnis * i
    gib_zurück ergebnis

wenn __name__ == "__main__":
    print(fakultät(5))
    print(math.sqrt(2))
```

## Wie es funktioniert

- **`deutschpython/keywords.py`** – Abbildung der 31 übersetzten
  Python-Schlüsselwörter (`wenn` → `if`, `für` → `for`, `klasse` → `class`, …).
- **`deutschpython/transpiler.py`** – nutzt das `tokenize`-Modul, um
  *ausschließlich* NAME-Token zu ersetzen, die exakt einem deutschen
  Schlüsselwort entsprechen. Strings, Kommentare, Zahlen und Attribut­zugriffe
  nach einem Punkt (`objekt.methode`) bleiben unverändert – deshalb
  funktionieren fremde Bibliotheken (die weiterhin Englisch sprechen)
  vollkommen normal.
- **`deutschpython/loader.py`** – ein Import-Hook, der `.dpy`-Dateien
  wie ganz normale `.py`-Module importierbar macht (`importiere` findet
  sowohl `.dpy`- als auch `.py`-Dateien).
- **`deutschpython/vokabular.py`** – optionale deutsche Namen für die
  gängigsten eingebauten Funktionen (`drucke`, `länge`, `bereich`, …) als
  ganz normale Zuweisungen, nicht als Ersetzung – dadurch besteht keine
  Gefahr, dass Parameter fremder Bibliotheken zerstört werden.
- **`deutschpython/stdlib/`** – deutsche Wrapper-Module für die zwölf
  meistgenutzten Teile der Standardbibliothek (siehe unten). Jedes Modul
  bindet die echten stdlib-Objekte nur unter deutschem Namen erneut ein,
  es wird nichts neu implementiert.

## Standardbibliothek auf Deutsch

```dpy
von deutschpython.stdlib importiere mathematik, zufall, datum

drucke(mathematik.wurzel(2))
drucke(zufall.ganzzahl(1, 6))
drucke(datum.heute())
```

| Modul | entspricht | Beispiele |
|---|---|---|
| `mathematik` | `math` | `wurzel`, `potenz`, `aufrunden`, `abrunden`, `fakultät`, `pi` |
| `zufall` | `random` | `zahl`, `ganzzahl`, `wahl`, `mische`, `stichprobe` |
| `zeit` | `time` | `jetzt`, `schlafe`, `formatiere` |
| `datum` | `datetime` | `Datum`, `Uhrzeit`, `Zeitstempel`, `Zeitspanne`, `heute`, `jetzt` |
| `betriebssystem` | `os` | `aktuelles_verzeichnis`, `erstelle_verzeichnis`, `umgebung` |
| `pfad` | `os.path` | `existiert`, `verbinde`, `basisname`, `ist_datei` |
| `system` | `sys` | `argumente`, `suchpfad`, `beenden`, `plattform` |
| `json` | `json` | `lade`, `speichere`, `lade_zeichenkette`, `speichere_als_zeichenkette` |
| `sammlungen` | `collections` | `Zähler`, `Schlange`, `GeordnetesWörterbuch`, `benannter_tupel` |
| `statistik` | `statistics` | `mittelwert`, `median`, `standardabweichung`, `varianz` |
| `text` | `re` | `suche`, `passt`, `finde_alle`, `ersetze`, `teile`, `kompiliere` |
| `funktional` | `itertools` + `functools` | `reduziere`, `kombinationen`, `permutationen`, `kette` |

Siehe `beispiele/standardbibliothek.dpy` für ein Beispiel. Weil hinter jedem
deutschen Namen exakt dasselbe stdlib-Objekt steckt, funktioniert alles
(Fehlerklassen, Rückgabetypen, Performance) genau wie im Original –
nur eben unter deutschem Namen ansprechbar.

## Installation & Nutzung

```bash
pip install -e .
dpy beispiele/hallo_welt.dpy
```

Ein `.dpy`-Skript kann normale `.py`-Module importieren und umgekehrt kann
ein normales `.py`-Skript (nach `import deutschpython; deutschpython.installiere()`)
auch `.dpy`-Module importieren.

## VS Code

Siehe [`vscode-deutschpython/README.md`](vscode-deutschpython/README.md) und
die ausführliche [`vscode-deutschpython/INSTALLATION.md`](vscode-deutschpython/INSTALLATION.md)
(mit Alternativen, falls „Install from Location..." bei dir fehlt).
Kurzfassung: `.dpy`-Dateien werden einer eigenen Sprach-ID zugeordnet
(nicht `python`), damit Pylance/der Python-Linter sie gar nicht erst prüft
und keine falschen Fehler anzeigt. Mit der optionalen Erweiterung kommt
zusätzlich Syntax-Hervorhebung und ein „Ausführen“-Button dazu.

## Tests

```bash
pip install pytest
pytest
```

## Grenzen (bewusste Vereinfachungen einer „dummen Idee“)

- Nur die Python-**Schlüsselwörter** werden übersetzt, keine eingebauten
  Funktionsnamen (siehe `vokabular.py` für eine sichere Opt-in-Alternative)
  und keine Bibliotheksnamen – Pakete werden weiterhin auf Englisch
  angesprochen.
- Fehlermeldungen, Tracebacks und `--help`-Texte der Standardbibliothek
  bleiben Englisch, da nur der Quelltext übersetzt wird, nicht CPython
  selbst.
- Die strukturelle Mustererkennung (`match`/`case`) wird nicht übersetzt,
  da es sich um kontextabhängige "weiche" Schlüsselwörter handelt.
