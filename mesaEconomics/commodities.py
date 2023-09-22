from typing import Any


class Commodity:
    """A commodity is an object with some predefined properties that can
    be consumed, produced, or traded.

    Attributes:
        unique_id: name of the commodity that is also used a unique identifier
    """

    _all_commodities: set[str | int] = set()

    def __init__(self, unique_id: str | int):
        # check that name is unique
        if unique_id in Commodity._all_commodities:
            raise ValueError(f"Commodity with name '{unique_id}' already exists")

        Commodity._all_commodities.add(unique_id)
        self.unique_id = unique_id

    def __repr__(self) -> str:
        return f"<Commodity {self.unique_id}>"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.unique_id == other.unique_id

    def __hash__(self):
        return hash(self.unique_id)

    @staticmethod
    def _clear():
        """Clear commodity list"""
        for o in Commodity._all_commodities:
            del o
        Commodity._all_commodities = set()
