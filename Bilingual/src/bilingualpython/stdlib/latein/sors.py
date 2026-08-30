"""Lateinischer Wrapper für das Modul ``random`` (sors = das Los, der Zufall)."""

from __future__ import annotations

import random as _random

numerus = _random.random
integer = _random.randint
electio = _random.choice
electiones = _random.choices
specimen = _random.sample
misce = _random.shuffle
pone_semen = _random.seed
