from typing import Optional

from rl.episode import DiscreteEpisode
from rl.regressor import FittingData


class LearningAlgorithm:
    """
    A learning algorithm that translates the episodes of past
    interactions into fitting data for the Regressor.

    Different learning algorithms are for example MonteCarlo or
    Temporal Difference Learning. Some learning algorithms could
    wait until a certain condition is given, before releasing fitting
    data for the Regressor. This is the reason that observe() returns
    an Optional.
    """

    def observe(self, episode: DiscreteEpisode) \
            -> Optional[FittingData]:
        """
        Observes the episode and may return a FittingData object,
        containing the data samples for the Regressor to fit on.
        :param episode: The latest episode.
        :return: Either None or the fitting data for the Regressor.
        """
        raise NotImplementedError
