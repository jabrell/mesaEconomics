import mesa
from .adopters import Adopter
from mesaEconomics.economies import Economy
from mesaEconomics.commodities import Commodity
import logging


class AdoptionModel(Economy):
    """A simple model of technology adoption

    Attributes:
        adoption_shares: Percentage of agents that adopted the technology
    """

    def __init__(
        self, agents: list[Adopter] = [], commodities: list[Commodity] = [], _seed=None
    ):
        # activation order does not matter
        schedule = mesa.time.BaseScheduler(model=self)
        super().__init__(
            agents=agents, commodities=commodities, schedule=schedule, _seed=_seed
        )

        # reporters
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "adoption": lambda m: {
                    t.unique_id: v for t, v in m.adoption_shares.items()
                }
            }
        )

    def compute_adoption_shares(self):
        self.adoption_shares = {c: 0 for c in self.commodities}
        for c in self.commodities:
            for a in self.agents:
                self.adoption_shares[c] += int(a.adopted_technologies.get(c, 0))
            self.adoption_shares[c] = self.adoption_shares[c] / len(self.agents)

    def step(self):
        self.compute_adoption_shares()
        self.datacollector.collect(self)
        logging.info("---- Perform model step")
        self.schedule.step()
