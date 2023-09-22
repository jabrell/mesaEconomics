import pytest
from mesaEconomics.agents import Agent


def test_unique_name():
    """Commodity class should raise ValueError if name is duplicated"""
    a = Agent(1)
    with pytest.raises(ValueError):
        Agent(1)
