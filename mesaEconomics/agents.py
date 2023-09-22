import mesa


class Agent(mesa.Agent):
    """An agent is an object that is able to perform some action

    Agents are a subclass of the mesa.Agent class. There are two major
    differences compared to mesa.Agent:
        1. We allow the unique id to be a string (instead of only integer)
        2. The agent can be created without a model

    Attributes:
        unique_id: A unique numeric identified for the agent
        model: Instance of the model that contains the agent
        pos: Position of the agent
    """

    _all_agents: set[int] = set()
    _model: mesa.Model | None

    def __init__(
        self,
        unique_id: int | str | None,
        model: mesa.Model | None = None,
    ):
        if unique_id in Agent._all_agents:
            raise ValueError(f"Agent '{unique_id}' already exists")
        self.unique_id = unique_id
        Agent._all_agents.add(unique_id)

        if model is not None:
            self._model = model
        self.pos: mesa.Position | None = None

    def __repr__(self) -> str:
        return f"<Agent {self.unique_id}>"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.unique_id == other.unique_id

    def __hash__(self):
        return hash(self.unique_id)

    @property
    def model(self):
        if self._model is None:
            raise ValueError(f"Agent '{self.unique_id}' is not yet part of a model")
        return self._model

    @model.setter
    def model(self, m: mesa.Model):
        self._model = m

    @staticmethod
    def _clear():
        """Clear commodity list"""
        for o in Agent._all_agents:
            del o
        Agent._all_agents = set()
