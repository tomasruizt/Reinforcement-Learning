import unittest

from rl.learning_strategy.EmpiricalMonteCarlo import EmpiricalMonteCarlo
from rl.utils.UpdateRules import RunningAverage


class MonteCarloTest(unittest.TestCase):

    def test_update_estimate(self):
        states = [10, 11, 12, 13]
        rewards = range(len(states))
        events = list(zip(states, rewards))

        estimator = EmpiricalMonteCarlo(update_rule=RunningAverage())
        estimator.update_estimate(events)

        for idx, state in enumerate(states):
            self.assertEquals(estimator.estimate(state), sum(rewards[idx:]))

        estimator.update_estimate(events)
        estimator.update_estimate(events)

        for idx, state in enumerate(states):
            self.assertEquals(estimator.estimate(state), sum(rewards[idx:]))