# coding: utf-8

import pytest
from eu2020.common.name import Name


@pytest.mark.parametrize(
    "name1p, name5p",
    (
        ("Adam", "Adame"),
        ("Eliška", "Eliško"),
        ("Jana", "Jano"),
        ("Jarda", "Jardo"),
        ("Jaroslav", "Jaroslave"),
        ("Karel", "Karle"),
        ("Libor", "Libore"),
        ("Michal", "Michale"),
        ("Milan", "Milane"),
        ("Pavel", "Pavle"),
        ("Petr", "Petře"),
        ("Petra", "Petro"),
        ("Tomáš", "Tomáši"),
        ("Vladimír", "Vladimíre"),
        ("Vlastík", "Vlastíku"),
        ("Rudolf", "Rudolfe"),
    ),
)
def test_name_5p(name1p, name5p):
    name = Name(name1p, "m")
    assert name5p == name.get_name5p()
