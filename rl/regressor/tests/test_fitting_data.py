import unittest

import numpy as np

from .. import FittingData


class TestFittingData(unittest.TestCase):

    def test_incompatible_input_sizes_error_has_enough_information(self):
        num_of_samples = 3
        num_of_targets = num_of_samples - 1
        feature_dimension = 5
        variables = np.ones((num_of_samples, feature_dimension))
        targets = np.ones(num_of_targets)
        expected_regex = self.get_expected_regex(num_of_samples, num_of_targets)
        with self.assertRaisesRegex(AssertionError, expected_regex):
            FittingData(variables=variables, targets=targets)

    @staticmethod
    def get_expected_regex(num_vars, num_tars) -> str:
        return f"Variables: {num_vars}. Targets: {num_tars}"
