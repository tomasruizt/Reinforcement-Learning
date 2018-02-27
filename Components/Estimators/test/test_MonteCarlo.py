import unittest

from Components.Estimators.MonteCarlo import MonteCarlo
from Components.RL_utils.UpdateRules import RunningAverage


class MonteCarloTest(unittest.TestCase):

    def test_update_estimate(self):
        states = [10, 11, 12, 13]
        rewards = range(len(states))
        events = list(zip(states, rewards))

        estimator = MonteCarlo(update_rule=RunningAverage())
        estimator.update_estimate(events)

        for idx, state in enumerate(states):
            self.assertEquals(estimator.estimate(state), sum(rewards[idx:]))

        estimator.update_estimate(events)
        estimator.update_estimate(events)

        for idx, state in enumerate(states):
            self.assertEquals(estimator.estimate(state), sum(rewards[idx:]))