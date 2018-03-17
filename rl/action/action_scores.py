from typing import Sequence

import numpy

from rl.action import DiscreteAction


class DiscreteActionScores:
    """Container class that assigns a float score for every action."""

    def __init__(self, actions: Sequence[DiscreteAction],
                 scores: Sequence[float]):
        """
        Initializes the object with the input actions and their
        corresponding scores. Both inputs must have the same length.
        :param actions: A sequence actions of size (A), where A is the
        size of the action space.
        :param scores: A sequence of scores of size (A) as well, each
        score corresponds to an action.
        """
        self._validate_input(actions, scores)
        self.actions = actions
        self.scores = scores

    @staticmethod
    def _validate_input(actions, scores):
        actions_size = len(actions)
        probabilities_size = len(scores)
        assert actions_size == probabilities_size, \
            "Length of input 'actions' (%d) and of input 'scores' (%d)" \
            " is different." % (actions_size, probabilities_size)
        if isinstance(scores, numpy.ndarray):
            assert len(scores.shape) == 1
