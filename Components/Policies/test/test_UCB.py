import unittest
from itertools import zip_longest

from Components.Policies.UCB import UCB


class UCBTest(unittest.TestCase):
    def test_select_action_explores(self):
        policy = UCB()
        states = list(range(5))
        estimates = [0]*5

        indices = []
        estimates_new = []
        for _ in range(len(states)):
            action_state_estimate_triplets = zip_longest([], states, estimates)
            idx, estimate = policy.select_action(action_state_estimate_triplets)
            indices.append(idx)
            estimates_new.append(estimate)

        self.assertEqual(len(set(indices)), 5)
        self.assertEquals(estimates_new, sorted(estimates_new))
