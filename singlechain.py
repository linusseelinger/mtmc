import os
from pathlib import Path

import numpy as np
import umbridge

from proposals.proposals import RandomWalkProposal
from src.mtmlda.mlmcmc import MLAcceptRateEstimator
from src.mtmlda.sampler import MTMLDASampler

import settings


# ==================================================================================================
class result_settings:
    result_directory_path = Path("results") / Path("chain")
    overwrite_results = True



# ==================================================================================================
def set_up_sampler():
    ground_proposal = RandomWalkProposal(
        settings.proposal_settings.step_width,
        settings.proposal_settings.covariance,
        settings.proposal_settings.rng_seed,
    )
    accept_rate_estimator = MLAcceptRateEstimator(
        settings.accept_rate_settings.initial_guess,
        settings.accept_rate_settings.update_parameter,
    )
    sampler = MTMLDASampler(
        settings.sampler_setup_settings,
        settings.models,
        accept_rate_estimator,
        ground_proposal,
    )
    return sampler


def main():
    os.makedirs(
        result_settings.result_directory_path.parent, exist_ok=result_settings.overwrite_results
    )
    sampler = set_up_sampler()
    mcmc_chain = sampler.run(settings.sampler_run_settings)
    np.save(result_settings.result_directory_path, mcmc_chain)


if __name__ == "__main__":
    main()
