import numpy as np

from rl.action import DiscreteActionFeatures, DiscreteActionScores
from rl.regressor import Regressor, FittingData


class SGDLinearRegressor(Regressor):
    """
    This regressor uses a Linear Model to approximate an action
    score. It optimizes the parameters using Stochastic Gradient
    Descent with every single sample.
    """

    def __init__(self, initial_weights: np.ndarray = None, learning_rate=0.01):
        """
        Initializes a LinearRegressor with the input weights w, and
        input learning rate alpha, if given.
        :param initial_weights: A numpy array that represents the weights
        for linear regression.
        :param learning_rate: The learning rate for Stochastic Gradient
        Descent.
        """
        if initial_weights is not None:
            assert initial_weights.shape[1] == 1
        assert isinstance(learning_rate, float)
        self._weights = initial_weights
        self._learning_rate = learning_rate

    def predict(self, action_features: DiscreteActionFeatures) -> \
            DiscreteActionScores:
        """
        Approximate the action scores.
        :param action_features: An object with the actions and their
        corresponding features vectors.
        :return: An object with the actions and their corresponding
        scores.
        """
        if self._weights is None:
            any_action_feature = next(iter(action_features.values()))
            self._init_w(features_dim=len(any_action_feature))

        actions, features = zip(*action_features.items())
        scores = self._calculate_scores(np.array(features))
        return DiscreteActionScores(actions, scores.flatten())

    def _init_w(self, features_dim):
        self._weights = np.ones((features_dim + 1, 1))

    def _calculate_scores(self, features: np.ndarray):
        num_of_actions, features_dim = features.shape
        beta_intercept = np.ones((num_of_actions, 1))
        extended_features = np.hstack((features, beta_intercept))
        scores = extended_features.dot(self._weights)
        return scores

    def fit(self, fitting_data: FittingData):
        if self._weights is None:
            self._init_w(features_dim=len(fitting_data.variables[0]))

        for x, y in zip(fitting_data.variables, fitting_data.targets):
            self._single_sample_sgd(x, y)

    def _single_sample_sgd(self, x: np.ndarray, y: float):
        y_predicted = self._calculate_scores(x.reshape(1, -1))
        extended_feature = np.hstack((x, 1))
        gradient = 2 * (y_predicted-y) * extended_feature.reshape(-1, 1)
        self._weights -= self._learning_rate * gradient
