# Deutsch-Python – VS-Code-Erweiterung

Diese kleine, lokale Erweiterung sorgt dafür, dass `.dpy`-Dateien
(Python mit deutschen Schlüsselwörtern) in VS Code

- **eigene Syntax-Hervorhebung** bekommen (`source.dpy`, siehe
  `syntaxes/deutschpython.tmLanguage.json`), und
- **keine falschen Fehler** von Pylance/dem Python-Linter erhalten, weil
  `.dpy`-Dateien als eigenständige Sprache `deutschpython` registriert sind
  und nicht als `python` – die Python-Erweiterung analysiert sie deshalb
  gar nicht erst.

Zusätzlich gibt es einen Play-Button oben rechts im Editor
(„Deutsch-Python: Datei ausführen“), der die aktuelle Datei über den
`dpy`-Befehl (aus dem `deutschpython`-Paket, siehe `../README.md`) in
einem Terminal ausführt.

## Installation (lokal, ohne Marketplace)

Ausführliche Schritt-für-Schritt-Anleitung mit mehreren Alternativen
(auch für den Fall, dass „Install from Location...“ bei dir nicht
existiert): siehe [`INSTALLATION.md`](INSTALLATION.md).

Kurzfassung:

1. `deutschpython` installieren, damit der `dpy`-Befehl existiert:
   ```
   cd ..
   pip install -e .
   ```
2. In VS Code: Befehlspalette (`Strg+Umschalt+P`) → **„Extensions:
   Install from Location...“** → diesen Ordner (`vscode-deutschpython`)
   auswählen.

Ganz ohne Erweiterung funktioniert die Fehlervermeidung übrigens auch
schon über `../.vscode/settings.json`: Die Dateiendung `.dpy` wird dort
bereits einer eigenen Sprach-ID zugeordnet, sodass der Python-Linter sie
ignoriert – nur die hübsche Syntax-Hervorhebung fehlt dann.
