from applications.adoptionModel import Adopter, AdoptionModel, Technology
import pandas as pd
import numpy as np
import logging


def create_adoption_model(
    num_agents=1000, num_steps=100, bounds_adoption=(0.95, 1), bounds_network=(0.2, 0.9)
):
    technologies = [Technology("PV")]
    adopters = [
        Adopter(
            unique_id=i,
            adopted_technologies={t: False for t in technologies},
            adoption_threshold={
                t: np.random.uniform(*bounds_adoption) for t in technologies
            },
            network_threshold={
                t: 1 for t in technologies  # np.random.uniform(*bounds_network)
            },
        )
        for i in range(num_agents)
    ]

    model = AdoptionModel(agents=adopters, commodities=technologies)
    for _ in range(num_steps):
        model.step()
    df_res = (
        pd.DataFrame(model.datacollector.model_vars["adoption"])
        .reset_index()
        .assign(scenario="NetworkEffects")
    )

    # the same without network effects
    for a in adopters:
        for t in a.network_threshold:
            a.network_threshold[t] = 1
            a.adopted_technologies[t] = 0
    model = AdoptionModel(agents=adopters, commodities=technologies)
    for _ in range(num_steps):
        model.step()
    df_res = pd.concat(
        [
            df_res,
            pd.DataFrame(model.datacollector.model_vars["adoption"])
            .reset_index()
            .assign(scenario="NoNetwork"),
        ]
    )
    print("here")
