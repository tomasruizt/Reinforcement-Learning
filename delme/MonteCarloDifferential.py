from collections import defaultdict
from itertools import repeat

from Interfaces import Estimator

import numpy as np


class MonteCarloDifferential(Estimator):
    def __init__(self, initial_value_estimate=0, learning_rate=repeat(0.05)):
        self._estimation = defaultdict(lambda: initial_value_estimate)
        self._learning_rate = learning_rate

    def estimate(self, key):
        return self._estimation[key]

    def update_estimate(self, state_reward_pairs):
        states, rewards = zip(*state_reward_pairs)
        mc_value_estimation = np.flip(np.cumsum(np.flip(rewards, 0)), 0)
        learning_rate = next(self._learning_rate)
        for state, mc_value_sample in zip(states, mc_value_estimation):
            value = self._estimation[state]
            difference = mc_value_sample - value
            self._estimation[state] += learning_rate * difference

    def get_information(self):
        return self._estimation.copy()
