# coding: utf-8

import pytest
from eu2020.common.name import Name

@pytest.mark.parametrize(
    'name1p, name5p',
    (
        ("Adam", "Adame"),
        ("Eliška", "Eliško"),
        ("Jana", "Jano"),
        ("Jarda", "Jardo"),
        ("Jaroslav", "Jaroslave"),
        ("Petr", "Petře"),
        ("Petra", "Petro"),
        ("Tomáš", "Tomáši")
    )
)
def testName5p(name1p, name5p):
    name = Name(name1p, "m")
    assert(name5p == name.get_name5p())
