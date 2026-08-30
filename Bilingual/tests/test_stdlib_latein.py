import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import math
import os

from bilingualpython.stdlib.latein import (  # noqa: E402
    collectiones,
    dies,
    functionalis,
    json,
    mathematica,
    semita,
    sors,
    statistica,
    systema,
    tempus,
    textus,
)
from bilingualpython.vokabular import latein as vocabularium  # noqa: E402


def test_mathematica():
    assert mathematica.pi == math.pi
    assert mathematica.radix(9) == 3.0
    assert mathematica.superior(1.2) == 2
    assert mathematica.factorialis(5) == 120


def test_sors():
    sors.pone_semen(42)
    valor = sors.integer(1, 10)
    assert 1 <= valor <= 10


def test_tempus():
    assert tempus.nunc() > 0


def test_dies():
    hodie = dies.hodie()
    assert isinstance(hodie, dies.Dies)
    momentum = dies.nunc()
    assert isinstance(momentum, dies.Momentum)


def test_systema_et_semita():
    assert systema.directorium_actuale() == os.getcwd()
    assert semita.existit(__file__)
    assert semita.nomen_basis("/a/b/c.txt") == "c.txt"


def test_json():
    data = {"a": 1, "b": [1, 2, 3]}
    catena = json.serva_ut_catenam(data)
    assert json.onera_ex_catena(catena) == data


def test_collectiones():
    numerator = collectiones.Numerator("aabbbc")
    assert numerator["b"] == 3
    biga = collectiones.Biga([1, 2, 3])
    biga.appendleft(0)
    assert list(biga) == [0, 1, 2, 3]


def test_statistica():
    assert statistica.media([1, 2, 3, 4]) == 2.5
    assert statistica.mediana([1, 2, 3]) == 2


def test_textus():
    assert textus.inveni_omnia(r"\d+", "a1 b22 c333") == ["1", "22", "333"]
    assert textus.substitue(r"\s+", "_", "a b  c") == "a_b_c"


def test_functionalis():
    assert functionalis.contrahe(lambda a, b: a + b, [1, 2, 3, 4]) == 10
    assert list(functionalis.combinationes([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]


def test_vocabularium():
    assert vocabularium.scribe is print
    assert vocabularium.longitudo([1, 2, 3]) == 3
    assert vocabularium.summa([1, 2, 3]) == 6
    assert vocabularium.maximum([1, 5, 2]) == 5
