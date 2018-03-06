from collections import defaultdict
from itertools import repeat

import numpy as np

from rl.learning_strategy.ValueUpdateStrategy import ValueUpdateStrategy

# TODO: Match the signature of EstimationUpdater
class TDLambda(ValueUpdateStrategy):
    def __init__(self, initial_estimation=0, learning_rate=repeat(0.05), _lambda=0.9):
        self._estimate = defaultdict(lambda: initial_estimation)
        self._learning_rate = learning_rate
        self._lambda = _lambda

    def estimate(self, state):
        return self._estimate[state]

    def update_estimate(self, state_reward_pairs):
        """
        :param state_reward_pairs: history of tuples (state, reward)
        :return: None
        """
        flipped_pairs = np.flip(list(state_reward_pairs), axis=0)
        states_flipped, rewards_flipped = zip(*flipped_pairs)
        coefficients = self._coefficients()
        states_flipped, rewards_flipped = iter(states_flipped), iter(rewards_flipped)
        state_new = next(states_flipped)
        learning = next(self._learning_rate)
        for state_old in states_flipped:
            target = next(rewards_flipped) + self._estimate[state_new]
            difference = target - self._estimate[state_old]
            self._estimate[state_old] += learning * difference * next(coefficients)
            state_new = state_old

    def get_information(self):
        return self._estimate.copy()

    def _coefficients(self):
        coefficient = self._lambda
        while True:
            yield coefficient
            coefficient *= self._lambda
