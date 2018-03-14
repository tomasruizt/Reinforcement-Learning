from typing import Sequence

import numpy
from rl.action import DiscreteAction


class DiscreteActionFeatures:
    """Container class that assigns a featurized representation to
    every action."""

    def __init__(self, actions: Sequence[DiscreteAction],
                 features: numpy.ndarray):
        """
        Initializes the object with the input actions and features.
        Both inputs must have the same length.
        :param actions: A sequence of actions of size (A,) where A is
        the size of the action space.
        :param features: A numpy array of size (A, D) where D is the
        size of each action's features.
        """
        assert len(actions) == len(features)
        self.actions = actions
        self.features = features
