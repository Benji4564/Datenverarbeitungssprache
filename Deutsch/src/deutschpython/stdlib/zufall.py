"""Deutscher Wrapper für das Modul ``random``."""

from __future__ import annotations

import random as _random

zahl = _random.random
ganzzahl = _random.randint
bereichszahl = _random.randrange
gleichverteilung = _random.uniform
wahl = _random.choice
wahlmehrfach = _random.choices
stichprobe = _random.sample
mische = _random.shuffle
setze_startwert = _random.seed
normalverteilung = _random.gauss
