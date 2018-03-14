from typing import Sequence

import numpy


class FittingData:
    """A container with variables and targets for the regressor to fit
    on."""

    def __init__(self, variables: numpy.ndarray, targets: Sequence[float]):
        """"
        Initializes the object with the given input variables and
        targets. Both inputs must have the same length.
        :param variables: A numpy array of size (N, D), where N is the
        number of samples to train on, and D is the size of each
        action's features.
        :param targets: A numpy array of size (N, 1) with a single
        scalar target for each sample in the input variables.
        """
        assert len(variables) == len(targets)
        self.variables = variables
        self.targets = targets
