from collections import defaultdict
from itertools import repeat

from math import sqrt, log

import numpy as np

from Interfaces import Policy


class UCB(Policy):
    def __init__(self, exploration=repeat(2)):
        self._times_visited = defaultdict(lambda: 1)
        self._exploration = exploration
        self._step_number = 0

    def select_action(self, action_state_estimate_triplets):
        self._step_number += 1
        _, states, estimates = zip(*action_state_estimate_triplets)
        UCBs = []
        exploration = next(self._exploration)
        for state_new, estimate in zip(states, estimates):
            times_visited = self._times_visited[state_new]
            UCB = estimate + exploration * sqrt(log(self._step_number) / times_visited)
            UCBs.append(UCB)

        idx = np.random.choice(np.argwhere(UCBs == np.max(UCBs)).flatten())
        self._times_visited[states[idx]] += 1
        return idx, UCBs[idx]
