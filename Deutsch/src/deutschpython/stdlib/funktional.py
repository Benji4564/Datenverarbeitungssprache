"""Deutscher Wrapper für die meistgenutzten Teile von ``itertools`` und ``functools``."""

from __future__ import annotations

import functools as _functools
import itertools as _itertools

reduziere = _functools.reduce
zwischenspeicher = _functools.cache
teilanwendung = _functools.partial

kette = _itertools.chain
zähle = _itertools.count
wiederhole = _itertools.repeat
kombinationen = _itertools.combinations
permutationen = _itertools.permutations
produkt = _itertools.product
gruppiere = _itertools.groupby
