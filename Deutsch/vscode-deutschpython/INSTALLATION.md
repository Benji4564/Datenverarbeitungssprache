# Installationsanleitung: Deutsch-Python-Erweiterung für VS Code

Diese Erweiterung sorgt dafür, dass `.dpy`-Dateien in VS Code Syntax-
Hervorhebung bekommen und **nicht** vom Python-Linter (Pylance) mit
falschen Fehlern markiert werden. Es gibt drei Wege, sie zu installieren –
probiere sie in dieser Reihenfolge durch, je nachdem was deine VS-Code-
Version anbietet.

Voraussetzung für alle drei Wege: Das `deutschpython`-Paket muss
installiert sein, damit der `dpy`-Befehl existiert (wird für den
„Ausführen"-Button gebraucht):

```bash
cd Deutsch
pip install -e .
```

---

## Weg 1: „Install from Location..." (VS Code ab Version 1.89)

1. VS Code öffnen.
2. Befehlspalette öffnen: `Strg+Umschalt+P` (Windows/Linux) bzw.
   `Cmd+Umschalt+P` (Mac).
3. `Extensions: Install from Location...` eingeben und auswählen.
4. Im Dateidialog den Ordner `Deutsch/vscode-deutschpython` auswählen
   (den ganzen Ordner, keine einzelne Datei).
5. Bei Aufforderung das Fenster neu laden.

Falls dieser Befehl in deiner Befehlspalette nicht auftaucht, ist er in
deiner VS-Code-Version/deinem Setup nicht verfügbar → weiter mit Weg 2.

---

## Weg 2: Als `.vsix`-Datei packen und installieren (empfohlen, funktioniert überall)

Das ist der offizielle Weg und funktioniert in praktisch jeder VS-Code-
Version über die normale Extensions-Ansicht.

1. Node.js/npm wird benötigt (falls nicht vorhanden: von
   [nodejs.org](https://nodejs.org) installieren).
2. Packaging-Werkzeug installieren:
   ```bash
   npm install -g @vscode/vsce
   ```
3. Erweiterung packen:
   ```bash
   cd Deutsch/vscode-deutschpython
   vsce package --allow-missing-repository
   ```
   Das erzeugt eine Datei `deutschpython-0.1.0.vsix` in diesem Ordner.
4. In VS Code: Extensions-Ansicht öffnen (`Strg+Umschalt+X`).
5. Oben im Extensions-Panel auf das `...`-Menü klicken →
   **„Install from VSIX..."**.
6. Die eben erzeugte `.vsix`-Datei auswählen.
7. Bei Aufforderung das Fenster neu laden.

**Alternative ohne eigenes Paketieren:** Aus dem Terminal heraus, ohne
die grafische Oberfläche:

```bash
code --install-extension Deutsch/vscode-deutschpython/deutschpython-0.1.0.vsix
```

(setzt voraus, dass der `code`-Befehl in deinem Terminal verfügbar ist –
in VS Code über die Befehlspalette `Shell Command: Install 'code' command
in PATH` einrichtbar.)

---

## Weg 3: Manuell in den Extensions-Ordner kopieren (Notlösung)

Falls weder Weg 1 noch Weg 2 funktionieren, kannst du den Ordner direkt
in das Verzeichnis kopieren, aus dem VS Code beim Start automatisch alle
Erweiterungen lädt. Der Zielordnername muss dem Muster
`herausgeber.name-version` folgen.

**Linux/Mac:**
```bash
mkdir -p ~/.vscode/extensions
cp -r Deutsch/vscode-deutschpython ~/.vscode/extensions/deutschpython-lokal.deutschpython-0.1.0
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.vscode\extensions"
Copy-Item -Recurse Deutsch\vscode-deutschpython "$env:USERPROFILE\.vscode\extensions\deutschpython-lokal.deutschpython-0.1.0"
```

Danach VS Code **vollständig beenden und neu starten** (nicht nur
„Fenster neu laden" – der Erweiterungs-Ordner wird nur beim Programmstart
neu eingelesen).

---

## Überprüfen, ob es funktioniert hat

1. `Deutsch/beispiele/hallo_welt.dpy` in VS Code öffnen.
2. Unten rechts in der Statusleiste sollte als Sprachmodus **„Deutsch-
   Python"** stehen (nicht „Python").
3. Schlüsselwörter wie `wenn`, `für`, `klasse`, `importiere` sollten
   farbig hervorgehoben sein.
4. Es sollten **keine** roten Wellenlinien/Fehler unter den deutschen
   Schlüsselwörtern erscheinen.
5. Oben rechts im Editor-Tab sollte ein ▶-Play-Button erscheinen, der
   die Datei über `dpy` in einem Terminal ausführt.

### Falls die Sprache trotzdem noch „Python" anzeigt

Unten rechts auf den Sprachmodus klicken → „Deutsch-Python" manuell
auswählen. Das passiert einmalig, danach merkt sich VS Code die
Zuordnung für `.dpy`-Dateien über die `files.associations`-Einstellung
in `Deutsch/.vscode/settings.json` (die bereits im Projekt liegt).

### Falls trotzdem noch rote Fehler von Pylance erscheinen

Das bedeutet meist, dass die Datei noch als „Python" statt
„Deutsch-Python" erkannt wird (siehe oben) – prüfe die Statusleiste.
