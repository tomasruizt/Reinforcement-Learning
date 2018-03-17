import unittest
from numpy.random import random as random_matrix
import numpy as np

from rl.action import DiscreteActionFeatures, DiscreteAction
from rl.regressor import SGDLinearRegressor, FittingData


class LinearRegressorTest(unittest.TestCase):

    PRECISION = 1e-10

    def test_predict_scores_are_scalars(self):
        regressor = SGDLinearRegressor()
        action_features = self._init_action_features()

        action_scores = regressor.predict(action_features)

        for score in action_scores.scores:
            dim_score = len(score)
            self.assertEqual(dim_score, 1)  # Is scalar

    def test_predict_does_linear_regression(self):
        action_features = self._init_action_features()
        weights = self._get_initial_weights_for(action_features)
        regressor = SGDLinearRegressor(weights)

        action_scores = regressor.predict(action_features)
        for score, features in zip(action_scores.scores,
                                   action_features.features):
            expected_score = features.dot(weights[:-1]) + weights[-1]
            self.assertAlmostEqual(expected_score, score, delta=self.PRECISION)

    def test_predict_input_actions_are_preserved(self):
        action_features = self._init_action_features()
        regressor = SGDLinearRegressor()
        action_scores = regressor.predict(action_features)

        expected_actions = action_features.actions
        self.assertEqual(expected_actions, action_scores.actions)

    def test_fit_updates_using_sgd(self):
        learning_rate = 0.01
        regressor = SGDLinearRegressor(learning_rate=learning_rate)
        fitting_data = self._init_fitting_data()
        regressor.fit(fitting_data)

        expected_weights = \
            self._get_expected_weights_after_sgd(fitting_data, learning_rate)
        self.assertTrue(np.allclose(expected_weights, regressor._weights,
                        atol=self.PRECISION))

    # Private methods

    @staticmethod
    def _get_initial_weights_for(action_features: DiscreteActionFeatures):
        weights = random_matrix((len(action_features.features[0]) + 1, 1))
        return weights

    @staticmethod
    def _init_action_features():
        features_dim = 6
        actions_list = [DiscreteAction(), DiscreteAction(), DiscreteAction]
        action_features = DiscreteActionFeatures(
            actions=actions_list,
            features=random_matrix((len(actions_list), features_dim))
        )
        return action_features

    @staticmethod
    def _init_fitting_data() -> FittingData:
        number_of_samples = 4
        features_dim = 7
        variables = random_matrix((number_of_samples, features_dim))
        targets = random_matrix((number_of_samples, 1))
        fitting_data = FittingData(variables, targets)
        return fitting_data

    def _get_expected_weights_after_sgd(self, fitting_data, learning_rate):
        features_dim = len(fitting_data.variables[0])
        expected_weights = np.ones((features_dim + 1, 1))
        for sample, target in zip(fitting_data.variables, fitting_data.targets):
            expected_weights = self._single_sample_sgd_step(
                expected_weights, learning_rate, sample, target)
        return expected_weights

    @staticmethod
    def _single_sample_sgd_step(
            expected_weights, learning_rate, sample, target):
        y_predicted = sample.dot(expected_weights[:-1]) + expected_weights[-1]
        extended_sample = np.hstack((sample, 1))
        gradient = 2 * (y_predicted-target) * extended_sample.reshape(-1, 1)
        expected_weights -= learning_rate * gradient
        return expected_weights
