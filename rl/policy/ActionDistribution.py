from typing import List

import numpy


class ActionDistribution:
    def __init__(self, actions: List[str], probabilities: numpy.ndarray):
        self._validate_input(actions, probabilities)
        self.actions = actions
        self.probabilities = probabilities

    @staticmethod
    def _validate_input(actions, probabilities):
        actions_size = len(actions)
        probabilities_size = len(probabilities)
        assert actions_size == probabilities_size, "Length of input 'actions' (%d) and of input 'probabilities' (%d) " \
                                                   "is different." % (actions_size, probabilities_size)
        total_sum = probabilities.sum()
        assert total_sum == 1, "Elements of input array 'probabilities' sum up to %f instead of 1." % total_sum
