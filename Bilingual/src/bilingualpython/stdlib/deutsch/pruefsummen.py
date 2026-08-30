"""Deutscher Wrapper für das Modul ``hashlib``.

Die Algorithmusnamen (md5, sha256, …) sind international übliche
Eigennamen und bleiben deshalb unverändert – nur das Modul selbst und die
generische Fabrikfunktion bekommen einen deutschen Namen.
"""

from __future__ import annotations

import hashlib as _hashlib

neue_prüfsumme = _hashlib.new
md5 = _hashlib.md5
sha1 = _hashlib.sha1
sha256 = _hashlib.sha256
sha512 = _hashlib.sha512
