from itertools import repeat

import numpy as np

from Components.Interfaces import Policy


class EpsilonGreedy(Policy):
    def __init__(self, exploration_rate=repeat(0.1)):
        self._exploration_rate = exploration_rate

    def select_action(self, action_state_estimate_triplets):
        _, _, action_estimates = zip(*action_state_estimate_triplets)

        if np.random.random() < next(self._exploration_rate):
            idx = np.random.randint(0, high=len(action_estimates))
            estimate = "RANDOM ACTION"
        else:
            idx = np.random.choice(np.argwhere(action_estimates == np.max(action_estimates)).flatten())
            estimate = action_estimates[idx]

        return idx, estimate
