# Bilingual-Python – VS-Code-Erweiterung

Diese kleine, lokale Erweiterung sorgt dafür, dass fremdsprachige
Python-Dateien in VS Code

- **eigene Syntax-Hervorhebung** bekommen:
  - `.dpy` (Deutsch) → `syntaxes/deutschpython.tmLanguage.json`
  - `.lpy` (Latein) → `syntaxes/lateinpython.tmLanguage.json`
- **keine falschen Fehler** von Pylance/dem Python-Linter erhalten, weil
  diese Dateien als eigenständige Sprachen (`deutschpython` bzw.
  `lateinpython`) registriert sind und nicht als `python` – die
  Python-Erweiterung analysiert sie deshalb gar nicht erst.

Zusätzlich gibt es einen Play-Button oben rechts im Editor
(„Bilingual-Python: Datei ausführen"), der die aktuelle Datei je nach
Endung über `dpy` oder `lpy` (aus dem `bilingualpython`-Paket, siehe
`../README.md`) in einem Terminal ausführt.

## Installation (lokal, ohne Marketplace)

Ausführliche Schritt-für-Schritt-Anleitung mit mehreren Alternativen
(auch für den Fall, dass „Install from Location..." bei dir nicht
existiert), inklusive Update-Anleitung: siehe
[`INSTALLATION.md`](INSTALLATION.md).

Kurzfassung:

1. `bilingualpython` installieren, damit die Befehle `dpy` und `lpy`
   existieren:
   ```
   cd ..
   pip install -e .
   ```
2. In VS Code: Befehlspalette (`Strg+Umschalt+P`) → **„Extensions:
   Install from Location...“** → diesen Ordner (`vscode-bilingualpython`)
   auswählen.

Ganz ohne Erweiterung funktioniert die Fehlervermeidung übrigens auch
schon über `../.vscode/settings.json`: Die Dateiendungen `.dpy` und
`.lpy` werden dort bereits eigenen Sprach-IDs zugeordnet, sodass der
Python-Linter sie ignoriert – nur die hübsche Syntax-Hervorhebung fehlt
dann.

## Eine weitere Sprache ergänzen

1. Grammatik-Datei nach dem Muster von `syntaxes/lateinpython.tmLanguage.json`
   anlegen (Scope-Name `source.<endung>`).
2. Eine `language-configuration.<sprache>.json` anlegen (Einrückungsregeln
   mit den neuen Schlüsselwörtern).
3. In `package.json` unter `contributes.languages` und
   `contributes.grammars` eintragen, plus die Endung im `when`-Ausdruck
   des Menüpunkts ergänzen.
4. In `extension.js` die Dateiendung in `BEFEHL_JE_ENDUNG` eintragen.
