import unittest
from itertools import repeat
import numpy

from rl.action import DiscreteActionScores, DiscreteAction
from rl.explorator.epsilon_greedy import EpsilonGreedy


class EpsilonGreedyTest(unittest.TestCase):

    def test_choose_action_deterministic_choice(self):
        action_scores = self._init_action_scores()
        expected_greedy_action = self._get_greedy_action_of(action_scores)

        deterministic_rate = repeat(0)
        e_greedy = EpsilonGreedy(exploration_rate=deterministic_rate, seed=0)
        chosen_action = e_greedy.choose_action(action_scores)
        self.assertEqual(expected_greedy_action, chosen_action)

    def test_choose_action_random_choice(self):
        action_scores = self._init_action_scores()
        greedy_action = self._get_greedy_action_of(action_scores)

        exploration_only = repeat(1)
        e_greedy = EpsilonGreedy(exploration_rate=exploration_only, seed=0)
        chosen_action = e_greedy.choose_action(action_scores)
        chosen_action_two = e_greedy.choose_action(action_scores)

        self.assertNotEqual(greedy_action, chosen_action)
        self.assertNotEqual(chosen_action, chosen_action_two)

    def test_choose_action_reject_none(self):
        e_greedy = EpsilonGreedy()
        with self.assertRaisesRegex(AssertionError, "Input 'action_scores' "
                                                    "should not be None."):
            e_greedy.choose_action(None)

    # Private methods

    @staticmethod
    def _init_action_scores():
        scores = [0.1, 0.3, 0.1, 0.4]
        action_scores = DiscreteActionScores(
            actions=[DiscreteAction() for _ in range(len(scores))],
            scores=scores
        )
        return action_scores

    @staticmethod
    def _get_greedy_action_of(action_scores: DiscreteActionScores) -> \
            DiscreteAction:
        highest_score_index = numpy.argmax(action_scores.scores)
        expected_greedy_action = action_scores.actions[highest_score_index]
        return expected_greedy_action
