from rl.action import DiscreteActionFeatures, DiscreteActionScores
from rl.regressor.fitting_data import FittingData


class Regressor:
    """A regressor to approximate values"""

    def predict(self, action_features: DiscreteActionFeatures)\
            -> DiscreteActionScores:
        """
        Approximates the scores for each action using its features.
        :param action_features: An object containing each action in the
        action space and their corresponding features.
        :return: An object containing each action in the action space
        and their corresponding score.
        """
        raise NotImplementedError

    def fit(self, fitting_data: FittingData):
        """
        Fit the regressor on the input FittingData object, which
        contains a sample of variables and targets to train on.
        :param fitting_data: The object with the training data samples.
        :return: None
        """
        raise NotImplementedError
