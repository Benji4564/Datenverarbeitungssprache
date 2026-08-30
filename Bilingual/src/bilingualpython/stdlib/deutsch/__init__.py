"""Deutsche Wrapper-Module für die zwölf meistgenutzten Teile der Python-
Standardbibliothek.

Jedes Modul hier importiert schlicht die echten Objekte aus der Standard-
bibliothek und bindet sie unter deutschen Namen erneut ein
(``wurzel = math.sqrt`` usw.). Es wird nichts neu implementiert – Verhalten,
Fehlerklassen und Performance sind exakt wie beim Original, nur der Name ist
Deutsch. Dadurch bleibt alles vollständig kompatibel mit Code, der die
englischen Originale erwartet (z. B.
``bilingualpython.stdlib.deutsch.mathematik.pi is math.pi``).

Verfügbare Module:
    mathematik     -> math
    zufall         -> random
    zeit           -> time
    datum          -> datetime
    betriebssystem -> os
    pfad           -> os.path
    pfadobjekte    -> pathlib
    system         -> sys
    json           -> json (nur deutsche Funktionsnamen)
    csv            -> csv (nur deutsche Funktionsnamen)
    sammlungen     -> collections
    statistik      -> statistics
    text           -> re
    funktional     -> itertools + functools
    dateiverwaltung -> shutil
    prozess        -> subprocess
    nebenlaeufigkeit -> threading
    protokoll      -> logging
    argumentanalyse -> argparse
    pruefsummen    -> hashlib
    kennung        -> uuid
    aufzaehlung    -> enum
    datenklassen   -> dataclasses
    kopie          -> copy

Wichtig: Nur die wichtigsten Einstiegspunkte jedes Moduls (Top-Level-
Funktionen, Konstanten, die zentrale(n) Klasse(n)) sind übersetzt. Methoden
auf den zurückgegebenen Objekten (z. B. `Argumentparser().add_argument(...)`
oder `Faden().start()`) bleiben auf Englisch, weil sie direkt von der
jeweiligen Bibliothek stammen.
"""
