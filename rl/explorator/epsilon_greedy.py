from itertools import repeat
import numpy as np

from rl.action import DiscreteAction, DiscreteActionScores
from rl.explorator import DiscreteExplorator


class EpsilonGreedy(DiscreteExplorator):
    """
    The Epsilon Greedy Explorator explores one of the actions
    available at random with a probability 0 <= p <= 1. Otherwise,
    it will select the choose the action with the highest score.
    """

    def __init__(self, exploration_rate=repeat(0.1), seed=None):
        """
        Initializes the EpsilonGreedy Explorator with an exploration
        rate that can change over time. By default, it is generator
        which repeats 0.1 indefinitely. For reproducibility, you can
        set the random seed as well.
        :param exploration_rate: Generator that determines the
        exploration rate.
        :param seed: The random seed.
        """
        self._exploration_rate = exploration_rate
        if seed is not None:
            np.random.seed(seed)

    def choose_action(self, action_scores: DiscreteActionScores) -> \
            DiscreteAction:
        assert action_scores is not None, "Input 'action_scores' should not " \
                                          "be None."
        current_exploration_probability = next(self._exploration_rate)
        assert 0 <= current_exploration_probability <= 1

        if np.random.random() < current_exploration_probability:
            return self._explore(action_scores)
        else:
            return self._choose_action_greedily(action_scores)

    # Private methods

    @staticmethod
    def _explore(action_scores):
        return np.random.choice(action_scores.actions)

    @staticmethod
    def _choose_action_greedily(action_scores: DiscreteActionScores) ->\
            DiscreteAction:
        """Choose the action with the highest score. If several actions
        have the highest score, select at random among them."""
        scores = action_scores.scores
        max_indices = np.argwhere(np.array(scores) == np.max(scores)).flatten()
        chosen_action_idx = np.random.choice(max_indices)
        return action_scores.actions[chosen_action_idx]
