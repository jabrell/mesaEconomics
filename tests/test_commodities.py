import pytest
from mesaEconomics.commodities import Commodity


def test_unique_name():
    """Commodity class should raise ValueError if name is duplicated"""
    a = Commodity("A")
    with pytest.raises(ValueError):
        Commodity("A")
    Commodity._clear()


def test_equality():
    a = Commodity("A")
    assert a == a
