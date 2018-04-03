from typing import Optional

from rl.experience_tuple import ExperienceTuple
from rl.regressor import FittingData


class LearningAlgorithm:
    """
    A learning algorithm that translates experience tuples of past
    interactions into fitting data for the Regressor.

    Different learning algorithms are for example MonteCarlo or
    Temporal Difference Learning. Some learning algorithms could
    wait until a certain condition is given, before releasing fitting
    data for the Regressor. This is the reason that observe() returns
    an Optional.
    """

    def observe(self, experience_tuple: ExperienceTuple) \
            -> Optional[FittingData]:
        """
        Observes the experience tuple and may return a FittingData
        object, containing the data samples for the Regressor to fit on.
        :param experience_tuple: The latest experience tuple.
        :return: Either None or the fitting data for the Regressor.
        """
        raise NotImplementedError
