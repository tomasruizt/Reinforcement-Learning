from math import log, sqrt
import numpy as np

from Interfaces import Estimator
from Setting10x10.TenTimesTenAgent import TenTimesTenAgent
from collections import defaultdict


class UCBExplorer(TenTimesTenAgent):
    def __init__(self, state, actions_available, estimator: Estimator, exploration=1):
        super().__init__(state, actions_available)
        self._times_visited = defaultdict(lambda: 1) # To avoid division by zero
        self._estimator = estimator
        self._exploration = exploration

    def take_action(self):
        UCBs = []
        step_number = len(self._history_states_and_rewards)
        states_neighboring = self._get_states_neighboring()
        for state_neighbor in states_neighboring:
            times_visited = self._times_visited[state_neighbor]

            value = self._estimator.estimate(state_neighbor)
            UCB = value + self._exploration * sqrt(log(step_number) / times_visited)
            UCBs.append(UCB)

        idx = np.random.choice(np.argwhere(UCBs == np.max(UCBs)).flatten())
        taken_action = self._actions_available_current[idx]
        self._times_visited[states_neighboring[idx]] += 1

        self._history_actions.append(taken_action)
        self._history_actions_estimates.append(UCBs[idx])
        return self._state_current, taken_action

    def get_information(self):
        return self._estimator.get_information()

    def game_finished(self):
        self._estimator.update_estimate(self._history_states_and_rewards)
        super().game_finished()
