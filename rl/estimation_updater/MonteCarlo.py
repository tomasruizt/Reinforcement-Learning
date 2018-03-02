from collections import defaultdict

import numpy as np

from rl.estimation_updater.EstimationUpdater import EstimationUpdater
from rl.utils.UpdateRules import DifferentialUpdate, UpdateRule

# TODO: esitmate() does not comply to superclass interface.
class MonteCarlo(EstimationUpdater):
    def __init__(self, update_rule: UpdateRule=DifferentialUpdate(), initial_value_estimate=0):
        self._estimation = defaultdict(lambda: initial_value_estimate)
        self._update_rule = update_rule

    def update_estimate(self, state_reward_pairs):
        states, rewards = zip(*state_reward_pairs)
        mc_value_estimations = np.flip(np.cumsum(np.flip(rewards, 0)), 0)
        # Update estimation, using running average
        for state, mc_value_estimation in zip(states, mc_value_estimations):
            self._estimation[state] = self._update_rule.get_new_estimate(
                key=state,
                estimate_old=self._estimation[state],
                estimate_sample=mc_value_estimation)

    def estimate(self, state):
        return self._estimation[state]

    def get_information(self):
        return self._estimation.copy()
