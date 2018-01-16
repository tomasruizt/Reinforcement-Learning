import unittest
from itertools import zip_longest, repeat

from Policies.EpsilonGreedy import EpsilonGreedy

import numpy as np


class EpsilonGreedyTest(unittest.TestCase):

    def test_deterministic_choice(self):
        action_estimates = [0.1, 0.3, 0.1, 0.4, 0.1]
        highest_idx = 3
        action_state_estimate_triplets = zip_longest([], [], action_estimates)

        policy = EpsilonGreedy(exploration_rate=repeat(0))
        idx, estimate = policy.select_action(action_state_estimate_triplets)

        self.assertEqual(idx, highest_idx)
        self.assertEqual(estimate, action_estimates[highest_idx])

    def test_random_choice(self):
        policy = EpsilonGreedy(exploration_rate=repeat(1))
        np.random.seed(0)
        action_state_estimate_triplets = zip_longest([], [], [0])
        _, estimate = policy.select_action(action_state_estimate_triplets)

        self.assertEqual(estimate, "RANDOM ACTION")
