import logging
from mesaEconomics.agents import Agent
from mesaEconomics.commodities import Commodity


class Adopter(Agent):
    """An individual that chooses to adopt a technology

    Properties:
        adoption_threshold: threshold level for adoption normalized to
            be between zero and one. If the agents adoption score is above
            this level, she will adopt the technology
        network_threshold: A value between zero and one that determines when the
            technology is adopted due to network effects. If the economy-wide
            adoption share is above the threshold there is 50% chance that the
            consumer adopts
        adopted_technologies: dict[str, bool] = {}
    """

    adopted_technologies: dict[Commodity, bool] = {}

    def __init__(
        self,
        unique_id: int | str,
        adopted_technologies: dict[Commodity, bool],
        adoption_threshold: dict[Commodity, bool],
        network_threshold: dict[Commodity, bool],
    ):
        super().__init__(unique_id)
        self.adopted_technologies = adopted_technologies
        self.adoption_threshold = adoption_threshold
        self.network_threshold = network_threshold

    def step(self):
        """In each step the agent decides about the adoption
        of technologies. Technologies are adopted if
        - the adoption score is above the threshold level.
        - if economy-wide adoption is above the network threshold
        """
        for technology in self.adopted_technologies:
            # adopt if already adopted or adoption score above threshold or economy-wide
            # score above network-threshold
            self.adopted_technologies[technology] = (
                self.adopted_technologies[technology]
                or self.random.random() > self.adoption_threshold[technology]
                or self.model.adoption_shares[technology]
                > self.network_threshold[technology]
            )
        logging.info(f"Agent {self.unique_id} moved")
        pass
