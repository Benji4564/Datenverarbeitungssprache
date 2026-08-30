"""Lateinischer Wrapper für die meistgenutzten Teile von ``itertools`` und ``functools``."""

from __future__ import annotations

import functools as _functools
import itertools as _itertools

contrahe = _functools.reduce
memoria = _functools.cache
applicatio_partialis = _functools.partial

catena = _itertools.chain
numera = _itertools.count
repete = _itertools.repeat
combinationes = _itertools.combinations
permutationes = _itertools.permutations
productum = _itertools.product
coacerva = _itertools.groupby
