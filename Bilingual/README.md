# bilingualpython

Python mit fremdsprachigen Schlüsselwörtern – **voll kompatibel** mit dem
normalen Python-Ökosystem (pip-Pakete, Standardbibliothek, C-Erweiterungen
usw.), weil kein Fork von CPython gebaut wird. Stattdessen wird der
Quelltext vor der Ausführung token-für-token in echtes Python übersetzt
und ganz normal von deinem installierten CPython kompiliert.

Aktuell unterstützte Sprachen:

| Sprache | Dateiendung | Befehl | Beispielwort für `if` |
|---|---|---|---|
| Deutsch | `.dpy` | `dpy` | `wenn` |
| Latein | `.lpy` | `lpy` | `si` |

Weitere Sprachen lassen sich ergänzen, indem man in
`src/bilingualpython/keywords.py` ein neues Wörterbuch anlegt (siehe
„Eine weitere Sprache ergänzen" unten).

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

```lpy
importa math

functio factorialis(n):
    si n < 0:
        iace ValueError("n debet >= 0 esse")
    resultatum = 1
    pro i in range(2, n + 1):
        resultatum = resultatum * i
    redde resultatum

si __name__ == "__main__":
    print(factorialis(5))
    print(math.sqrt(2))
```

## Wie es funktioniert

- **`bilingualpython/keywords.py`** – ein Wörterbuch pro Sprache (Sprachwort
  → echtes Python-Schlüsselwort), zusammengeführt in der Registry
  `SPRACHEN` (Sprachcode, Dateiendung, Anzeigename).
- **`bilingualpython/transpiler.py`** – nutzt das `tokenize`-Modul, um
  *ausschließlich* NAME-Token zu ersetzen, die exakt einem Schlüsselwort
  der gewählten Sprache entsprechen (`uebersetze_quelltext(text, sprache)`).
  Strings, Kommentare, Zahlen und Attributzugriffe nach einem Punkt
  (`objekt.methode`) bleiben unverändert – deshalb funktionieren fremde
  Bibliotheken (die weiterhin Englisch sprechen) vollkommen normal.
- **`bilingualpython/loader.py`** – ein Import-Hook, der für jede
  registrierte Sprache ihre Dateiendung importierbar macht (`.dpy` und
  `.lpy` finden sich gegenseitig und normale `.py`-Module).
- **`bilingualpython/vokabular/`** – je ein Modul pro Sprache
  (`deutsch.py`, `latein.py`) mit optionalen Namen für die gängigsten
  eingebauten Funktionen, als ganz normale Zuweisungen statt als
  Ersetzung – dadurch besteht keine Gefahr, dass Parameter fremder
  Bibliotheken zerstört werden.
- **`bilingualpython/stdlib/`** – je ein Unterpaket pro Sprache
  (`deutsch/`, `latein/`) mit Wrapper-Modulen für die meistgenutzten
  Teile der Standardbibliothek (siehe unten). Jedes Modul bindet die
  echten stdlib-Objekte nur unter übersetztem Namen erneut ein, es wird
  nichts neu implementiert.

## Eine weitere Sprache ergänzen

1. In `keywords.py` ein neues `dict` anlegen (Sprachwort → Python-Wort)
   und in `SPRACHEN` mit Dateiendung + Anzeigename eintragen.
2. Optional: `vokabular/<sprache>.py` mit Namen für gängige Builtins.
3. Optional: `stdlib/<sprache>/` mit denselben Wrapper-Modulen wie bei
   Deutsch/Latein (gleiche Dateinamen sind nicht nötig, aber sinnvoll).
4. `pyproject.toml`: einen neuen `[project.scripts]`-Eintrag + Funktion
   in `bilingualpython/cli.py` ergänzen (`fuehre_aus("<sprache>", ...)`).
5. Für VS Code: siehe [`vscode-bilingualpython/README.md`](vscode-bilingualpython/README.md#eine-weitere-sprache-ergänzen).

## Standardbibliothek

```dpy
von bilingualpython.stdlib.deutsch importiere mathematik, zufall, datum
von bilingualpython.vokabular.deutsch importiere drucke

drucke(mathematik.wurzel(2))
drucke(zufall.ganzzahl(1, 6))
drucke(datum.heute())
```

```lpy
ex bilingualpython.stdlib.latein importa mathematica, sors, dies
ex bilingualpython.vokabular.latein importa scribe

scribe(mathematica.radix(2))
scribe(sors.integer(1, 6))
scribe(dies.hodie())
```

### Deutsch (`bilingualpython.stdlib.deutsch`)

| Modul | entspricht | Beispiele |
|---|---|---|
| `mathematik` | `math` | `wurzel`, `potenz`, `aufrunden`, `abrunden`, `fakultät`, `pi` |
| `zufall` | `random` | `zahl`, `ganzzahl`, `wahl`, `mische`, `stichprobe` |
| `zeit` | `time` | `jetzt`, `schlafe`, `formatiere` |
| `datum` | `datetime` | `Datum`, `Uhrzeit`, `Zeitstempel`, `Zeitspanne`, `heute`, `jetzt` |
| `betriebssystem` | `os` | `aktuelles_verzeichnis`, `erstelle_verzeichnis`, `umgebung` |
| `pfad` | `os.path` | `existiert`, `verbinde`, `basisname`, `ist_datei` |
| `pfadobjekte` | `pathlib` | `Pfad`, `heimatverzeichnis`, `aktuelles_verzeichnis` |
| `system` | `sys` | `argumente`, `suchpfad`, `beenden`, `plattform` |
| `json` | `json` | `lade`, `speichere`, `lade_zeichenkette`, `speichere_als_zeichenkette` |
| `csv` | `csv` | `leser`, `schreiber`, `Wörterbuchleser`, `Wörterbuchschreiber` |
| `sammlungen` | `collections` | `Zähler`, `Schlange`, `GeordnetesWörterbuch`, `benannter_tupel` |
| `statistik` | `statistics` | `mittelwert`, `median`, `standardabweichung`, `varianz` |
| `text` | `re` | `suche`, `passt`, `finde_alle`, `ersetze`, `teile`, `kompiliere` |
| `funktional` | `itertools` + `functools` | `reduziere`, `kombinationen`, `permutationen`, `kette` |
| `dateiverwaltung` | `shutil` | `kopiere`, `kopiere_baum`, `verschiebe`, `lösche_baum` |
| `prozess` | `subprocess` | `starte`, `öffne_prozess`, `Prozessfehler` |
| `nebenlaeufigkeit` | `threading` | `Faden`, `Sperre`, `Ereignis` |
| `protokoll` | `logging` | `hole_protokollierer`, `konfiguriere`, `FEHLER`, `WARNUNG` |
| `argumentanalyse` | `argparse` | `Argumentparser`, `Namensraum` |
| `pruefsummen` | `hashlib` | `sha256`, `md5`, `neue_prüfsumme` |
| `kennung` | `uuid` | `ID`, `zufalls_id`, `namensbasierte_id` |
| `aufzaehlung` | `enum` | `Aufzählung`, `Ganzzahlaufzählung`, `automatisch` |
| `datenklassen` | `dataclasses` | `datenklasse`, `feld`, `ist_datenklasse`, `zu_wörterbuch` |
| `kopie` | `copy` | `flache_kopie`, `tiefe_kopie` |

### Latein (`bilingualpython.stdlib.latein`)

| Modul | entspricht | Beispiele |
|---|---|---|
| `mathematica` | `math` | `radix`, `potentia`, `superior`, `inferior`, `factorialis`, `pi` |
| `sors` | `random` | `numerus`, `integer`, `electio`, `misce`, `specimen` |
| `tempus` | `time` | `nunc`, `dormi`, `formata` |
| `dies` | `datetime` | `Dies`, `Hora`, `Momentum`, `Intervallum`, `hodie`, `nunc` |
| `systema` | `os` | `directorium_actuale`, `crea_directorium`, `ambitus` |
| `semita` | `os.path` | `existit`, `iunge`, `nomen_basis`, `est_charta` |
| `processus` | `sys` | `argumenta`, `semita_quaestionis`, `exi`, `suggestum` |
| `json` | `json` | `onera`, `serva`, `onera_ex_catena`, `serva_ut_catenam` |
| `collectiones` | `collections` | `Numerator`, `Biga`, `LexiconOrdinatum`, `tuplum_nominatum` |
| `statistica` | `statistics` | `media`, `mediana`, `deviatio_standardis`, `variantia` |
| `textus` | `re` | `quaere`, `convenit`, `inveni_omnia`, `substitue`, `compone` |
| `functionalis` | `itertools` + `functools` | `contrahe`, `combinationes`, `permutationes`, `catena` |

Siehe `beispiele/*.dpy`, `beispiele/latein/*.lpy` für Beispiele. Weil
hinter jedem übersetzten Namen exakt dasselbe stdlib-Objekt steckt,
funktioniert alles (Fehlerklassen, Rückgabetypen, Performance) genau wie
im Original. Beachte: nur die wichtigsten Einstiegspunkte jedes Moduls
sind übersetzt, Methoden auf den zurückgegebenen Objekten (z. B.
`Argumentparser().add_argument(...)`) bleiben auf Englisch.

## Installation & Nutzung

```bash
pip install -e .
dpy beispiele/hallo_welt.dpy
lpy beispiele/latein/salve_mundi.lpy
```

Ein `.dpy`- oder `.lpy`-Skript kann normale `.py`-Module importieren und
sich gegenseitig importieren; umgekehrt kann ein normales `.py`-Skript
(nach `import bilingualpython; bilingualpython.installiere()`) auch
`.dpy`- und `.lpy`-Module importieren.

## VS Code

Siehe [`vscode-bilingualpython/README.md`](vscode-bilingualpython/README.md) und
die ausführliche [`vscode-bilingualpython/INSTALLATION.md`](vscode-bilingualpython/INSTALLATION.md)
(mit Alternativen, falls „Install from Location..." bei dir fehlt, und
einer Anleitung zum Aktualisieren). Kurzfassung: `.dpy`- und
`.lpy`-Dateien werden eigenen Sprach-IDs zugeordnet (nicht `python`),
damit Pylance/der Python-Linter sie gar nicht erst prüft und keine
falschen Fehler anzeigt. Mit der optionalen Erweiterung kommt zusätzlich
Syntax-Hervorhebung und ein „Ausführen"-Button dazu.

## Tests

```bash
pip install pytest
pytest
```

## Grenzen (bewusste Vereinfachungen einer „dummen Idee")

- Nur die Python-**Schlüsselwörter** werden übersetzt, keine eingebauten
  Funktionsnamen (siehe `vokabular/`-Module für eine sichere
  Opt-in-Alternative) und keine Bibliotheksnamen – Pakete werden
  weiterhin auf Englisch angesprochen.
- Fehlermeldungen, Tracebacks und `--help`-Texte der Standardbibliothek
  bleiben Englisch, da nur der Quelltext übersetzt wird, nicht CPython
  selbst.
- Die strukturelle Mustererkennung (`match`/`case`) wird nicht übersetzt,
  da es sich um kontextabhängige "weiche" Schlüsselwörter handelt.
- Die lateinischen Wörter sind eine pragmatische Auswahl (teils klassisches
  Latein wie `si`, `dum`, `cum`, `non`, `est`; teils neu gebildete
  Imperative wie `redde` für „return"), keine linguistisch geprüfte
  Terminologie.
