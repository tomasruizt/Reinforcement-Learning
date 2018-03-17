from typing import List

import numpy


class StateActionValues:
    """
    A container object with a corresponding value for each state-action pair.
    """

    def __init__(self, state_actions: List, values: numpy.ndarray):
        """
        Initializes a instance with the given input. Both parameters must have the same length.
        :param state_actions: The state-action pairs.
        :param values: The values corresponding to the state-action pairs.
        """
        self._check_input_same_length(state_actions, values)
        self.state_actions = state_actions
        self.values = values

    @staticmethod
    def _check_input_same_length(state_actions, values):
        length_values = len(values)
        length_state_actions = len(state_actions)
        assert length_state_actions == length_values, "Length of inputs 'state_actions' and 'values' is different: %d" \
                                                      " and %d, respectively " % (length_state_actions, length_values)
