import mesa
from .agents import Agent
from .commodities import Commodity


class Economy(mesa.Model):
    """An economy is a mesa model characterized by agents and
    commodities
    """

    _agents: list[Agent] = []
    _commodities: list[Commodity] = []

    def __init__(
        self,
        agents: list[Agent] = [],
        commodities: list[Commodity] = [],
        schedule: mesa.time.BaseScheduler | None = None,
        _seed: int | None = None,
    ):
        """
        Args:
            agents: list of agents in the economy
        """
        super().__init__(_seed=_seed)
        if schedule is None:
            self.schedule = mesa.time.BaseScheduler(self)
        else:
            self.schedule = schedule
        self.add_agents(agents)
        self._commodities = commodities

    @property
    def agents(self):
        return self._agents

    def add_agents(self, agents: list[Agent] | Agent):
        if isinstance(agents, Agent):
            agents = [agents]
        for a in agents:
            a.model = self
            self.schedule.add(a)
        self._agents.extend(agents)

    @property
    def commodities(self):
        return self._commodities
