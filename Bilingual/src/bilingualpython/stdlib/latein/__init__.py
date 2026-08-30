"""Lateinische Wrapper-Module für die zwölf meistgenutzten Teile der Python-
Standardbibliothek.

Jedes Modul hier importiert schlicht die echten Objekte aus der Standard-
bibliothek und bindet sie unter lateinischem Namen erneut ein
(``radix = math.sqrt`` usw.). Es wird nichts neu implementiert – Verhalten,
Fehlerklassen und Performance sind exakt wie beim Original. Dadurch bleibt
alles vollständig kompatibel mit Code, der die englischen Originale
erwartet (z. B. ``bilingualpython.stdlib.latein.mathematica.pi is math.pi``).

Verfügbare Module:
    mathematica -> math
    sors        -> random
    tempus      -> time
    dies        -> datetime
    systema     -> os
    semita      -> os.path
    processus   -> sys
    json        -> json (nur lateinische Funktionsnamen)
    collectiones -> collections
    statistica  -> statistics
    textus      -> re
    functionalis -> itertools + functools

Wichtig: Nur die wichtigsten Einstiegspunkte jedes Moduls (Top-Level-
Funktionen, Konstanten, die zentrale(n) Klasse(n)) sind übersetzt. Methoden
auf den zurückgegebenen Objekten bleiben auf Englisch, weil sie direkt von
der jeweiligen Bibliothek stammen.
"""
