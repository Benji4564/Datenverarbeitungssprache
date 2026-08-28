"""Deutsche Wrapper-Module für die zwölf meistgenutzten Teile der Python-
Standardbibliothek.

Jedes Modul hier importiert schlicht die echten Objekte aus der Standard-
bibliothek und bindet sie unter deutschen Namen erneut ein
(``wurzel = math.sqrt`` usw.). Es wird nichts neu implementiert – Verhalten,
Fehlerklassen und Performance sind exakt wie beim Original, nur der Name ist
Deutsch. Dadurch bleibt alles vollständig kompatibel mit Code, der die
englischen Originale erwartet (z. B. ``deutschpython.stdlib.mathematik.pi
is math.pi``).

Verfügbare Module:
    mathematik   -> math
    zufall       -> random
    zeit         -> time
    datum        -> datetime
    betriebssystem -> os
    pfad         -> os.path
    system       -> sys
    json         -> json (nur deutsche Funktionsnamen)
    sammlungen   -> collections
    statistik    -> statistics
    text         -> re
    funktional   -> itertools + functools
"""
