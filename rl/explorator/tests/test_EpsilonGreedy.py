import unittest
from itertools import repeat
from typing import Sequence

import numpy

from rl.action import DiscreteActionScores, DiscreteAction
from rl.explorator.epsilon_greedy import EpsilonGreedy


class EpsilonGreedyTest(unittest.TestCase):

    def test_deterministic_choice(self):
        scores = [0.1, 0.3, 0.1, 0.4]
        action_scores = self._init_action_scores_for(scores)
        deterministic_rate = repeat(0)
        e_greedy = EpsilonGreedy(exploration_rate=deterministic_rate, seed=0)

        chosen_action = e_greedy.choose_action(action_scores)
        expected_greedy_action = action_scores.actions[numpy.argmax(scores)]
        self.assertEqual(expected_greedy_action, chosen_action)

    def test_random_choice(self):
        pass

    # Private methods

    @staticmethod
    def _init_action_scores_for(scores: Sequence[float]):
        action_scores = DiscreteActionScores(
            actions=[DiscreteAction() for _ in range(len(scores))],
            scores=scores
        )
        return action_scores
