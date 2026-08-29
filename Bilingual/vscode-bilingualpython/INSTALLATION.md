# Installationsanleitung: Bilingual-Python-Erweiterung für VS Code

Diese Erweiterung sorgt dafür, dass `.dpy`-Dateien (Deutsch) und
`.lpy`-Dateien (Latein) in VS Code Syntax-Hervorhebung bekommen und
**nicht** vom Python-Linter (Pylance) mit falschen Fehlern markiert
werden. Es gibt drei Wege, sie zu installieren – probiere sie in dieser
Reihenfolge durch, je nachdem was deine VS-Code-Version anbietet.

Voraussetzung für alle drei Wege: Das `bilingualpython`-Paket muss
installiert sein, damit die Befehle `dpy` und `lpy` existieren (werden
für den „Ausführen"-Button gebraucht):

```bash
cd Bilingual
pip install -e .
```

---

## Weg 1: „Install from Location..." (VS Code ab Version 1.89)

1. VS Code öffnen.
2. Befehlspalette öffnen: `Strg+Umschalt+P` (Windows/Linux) bzw.
   `Cmd+Umschalt+P` (Mac).
3. `Extensions: Install from Location...` eingeben und auswählen.
4. Im Dateidialog den Ordner `Bilingual/vscode-bilingualpython` auswählen
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
   cd Bilingual/vscode-bilingualpython
   vsce package --allow-missing-repository
   ```
   Das erzeugt eine Datei `bilingualpython-0.3.0.vsix` in diesem Ordner.
4. In VS Code: Extensions-Ansicht öffnen (`Strg+Umschalt+X`).
5. Oben im Extensions-Panel auf das `...`-Menü klicken →
   **„Install from VSIX..."**.
6. Die eben erzeugte `.vsix`-Datei auswählen.
7. Bei Aufforderung das Fenster neu laden.

**Alternative ohne eigenes Paketieren:** Aus dem Terminal heraus, ohne
die grafische Oberfläche:

```bash
code --install-extension Bilingual/vscode-bilingualpython/bilingualpython-0.3.0.vsix
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
cp -r Bilingual/vscode-bilingualpython ~/.vscode/extensions/bilingualpython-lokal.bilingualpython-0.3.0
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.vscode\extensions"
Copy-Item -Recurse Bilingual\vscode-bilingualpython "$env:USERPROFILE\.vscode\extensions\bilingualpython-lokal.bilingualpython-0.3.0"
```

Danach VS Code **vollständig beenden und neu starten** (nicht nur
„Fenster neu laden" – der Erweiterungs-Ordner wird nur beim Programmstart
neu eingelesen).

---

## Erweiterung aktualisieren

Wenn sich `package.json`, `extension.js`, eine Grammatik-Datei o. ä.
geändert haben (z. B. weil eine neue Sprache oder neue Schlüsselwörter
dazugekommen sind), muss VS Code die neue Version einlesen. Wie das geht,
hängt davon ab, welchen Weg du bei der Installation gewählt hast.

### Update bei Weg 1 (Install from Location)

Der schnellste Weg: „Install from Location..." legt bei Ordnern normaler-
weise einen **symbolischen Link** auf `Bilingual/vscode-bilingualpython`
an, statt die Dateien zu kopieren. Das heißt, Änderungen an den Dateien in
diesem Ordner werden automatisch übernommen – du musst die Erweiterung
**nicht neu installieren**:

1. Dateien wie gewohnt bearbeiten (bzw. `git pull`, falls die Änderungen
   aus dem Repository kommen).
2. Befehlspalette → **„Developer: Reload Window"** (oder VS Code einmal
   schließen und neu öffnen).

Falls die Änderungen danach nicht sichtbar sind (manche VS-Code-Versionen
kopieren statt zu verlinken), führe „Install from Location..." aus Weg 1
einfach erneut aus – ein erneuter Import überschreibt die alte Kopie.

### Update bei Weg 2 (.vsix)

Hier musst du neu packen und neu installieren:

1. Versionsnummer in `Bilingual/vscode-bilingualpython/package.json`
   erhöhen (Feld `"version"`, z. B. `0.3.0` → `0.3.1`). Das ist wichtig –
   VS Code erkennt eine neue Version am geänderten Versionsstring, nicht
   am Dateiinhalt.
2. Neu packen:
   ```bash
   cd Bilingual/vscode-bilingualpython
   vsce package --allow-missing-repository
   ```
3. Installieren:
   ```bash
   code --install-extension bilingualpython-0.3.1.vsix
   ```
   (Passe die Versionsnummer im Dateinamen an. Alternativ über die GUI:
   Extensions-Ansicht → `...`-Menü → „Install from VSIX...".)
4. Befehlspalette → **„Developer: Reload Window"**.

Falls VS Code die alte Version behält (z. B. weil du die Versionsnummer
vergessen hast zu erhöhen): die Erweiterung in der Extensions-Ansicht
suchen → **Uninstall** → VS Code neu starten → neue `.vsix` installieren.

### Update bei Weg 3 (manuelles Kopieren)

1. Alten Ordner löschen und durch den aktuellen Stand ersetzen:

   **Linux/Mac:**
   ```bash
   rm -rf ~/.vscode/extensions/bilingualpython-lokal.bilingualpython-0.3.0
   cp -r Bilingual/vscode-bilingualpython ~/.vscode/extensions/bilingualpython-lokal.bilingualpython-0.3.0
   ```

   **Windows (PowerShell):**
   ```powershell
   Remove-Item -Recurse -Force "$env:USERPROFILE\.vscode\extensions\bilingualpython-lokal.bilingualpython-0.3.0"
   Copy-Item -Recurse Bilingual\vscode-bilingualpython "$env:USERPROFILE\.vscode\extensions\bilingualpython-lokal.bilingualpython-0.3.0"
   ```
2. VS Code **vollständig beenden und neu starten** (ein reines „Reload
   Window" reicht bei dieser Methode nicht immer aus, weil der
   Erweiterungs-Ordner nur beim Programmstart neu eingelesen wird).

### Installierte Version prüfen / doppelte Versionen aufräumen

```bash
code --list-extensions --show-versions | grep -i bilingualpython
```

Falls von einer älteren Fassung dieses Projekts noch eine Erweiterung
namens `deutschpython` installiert ist, kann sie parallel bestehen bleiben
oder über die Extensions-Ansicht (`Strg+Umschalt+X`) entfernt werden –
sie wird von `bilingualpython` funktional abgelöst (Deutsch + jetzt auch
Latein).

Taucht `bilingualpython` mehrfach mit unterschiedlichen IDs auf (z. B.
weil du zwischendurch verschiedene Wege ausprobiert hast), über die
Extensions-Ansicht nach „Bilingual-Python" suchen und überzählige
Einträge mit **Uninstall** entfernen, bevor du neu installierst – sonst
kann es sein, dass VS Code die falsche (alte) Version aktiv hält.

---

## Überprüfen, ob es funktioniert hat

### Deutsch (`.dpy`)

1. `Bilingual/beispiele/hallo_welt.dpy` in VS Code öffnen.
2. Unten rechts in der Statusleiste sollte als Sprachmodus **„Deutsch-
   Python"** stehen (nicht „Python").
3. Schlüsselwörter wie `wenn`, `für`, `klasse`, `importiere` sollten
   farbig hervorgehoben sein.
4. Oben rechts im Editor-Tab sollte ein ▶-Play-Button erscheinen, der die
   Datei über `dpy` in einem Terminal ausführt.

### Latein (`.lpy`)

1. `Bilingual/beispiele/latein/salve_mundi.lpy` in VS Code öffnen.
2. Unten rechts in der Statusleiste sollte als Sprachmodus **„Latein-
   Python"** stehen.
3. Schlüsselwörter wie `si`, `pro`, `classis`, `importa` sollten farbig
   hervorgehoben sein.
4. Der gleiche ▶-Play-Button führt die Datei über `lpy` aus.

In beiden Fällen sollten **keine** roten Wellenlinien/Fehler unter den
fremdsprachigen Schlüsselwörtern erscheinen.

### Falls die Sprache trotzdem noch „Python" anzeigt

Unten rechts auf den Sprachmodus klicken → „Deutsch-Python" bzw.
„Latein-Python" manuell auswählen. Das passiert einmalig, danach merkt
sich VS Code die Zuordnung über die `files.associations`-Einstellung in
`Bilingual/.vscode/settings.json` (die bereits im Projekt liegt).

### Falls trotzdem noch rote Fehler von Pylance erscheinen

Das bedeutet meist, dass die Datei noch als „Python" statt als
„Deutsch-Python"/„Latein-Python" erkannt wird (siehe oben) – prüfe die
Statusleiste.
