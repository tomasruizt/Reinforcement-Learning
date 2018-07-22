import unittest

import numpy as np

from .. import DiscreteAction, DiscreteActionFeatures


class DiscreteActionFeaturesTest(unittest.TestCase):

    VALID_KEY = DiscreteAction()
    VALID_VALUE = np.ones(1)

    def test_mapping_is_from_discrete_action_to_numpy_array(self):
        valid_entry = (self.VALID_KEY, self.VALID_VALUE)
        DiscreteActionFeatures([valid_entry])

    def test_invalid_keys_are_not_discrete_action_features(self):
        invalid_keys = [None, "one", 2.0]
        for invalid_key in invalid_keys:
            invalid_entry = (invalid_key, self.VALID_VALUE)
            with self.assertRaises(AssertionError):
                DiscreteActionFeatures([invalid_entry])

    def test_invalid_value_is_not_numpy_array(self):
        invalid_values = [None, "two", 2.0]
        for invalid_value in invalid_values:
            invalid_entry = (self.VALID_KEY, invalid_value)
            with self.assertRaises(AssertionError):
                DiscreteActionFeatures([invalid_entry])

    @staticmethod
    def test_construction_with_dict():
        some_dict = {DiscreteAction(): np.ones(1)}
        DiscreteActionFeatures(some_dict)

    def test_all_values_must_have_same_lengths(self):
        invalid_entries = {
            DiscreteAction(): np.ones(2),
            DiscreteAction(): np.ones(3),
        }
        with self.assertRaises(AssertionError):
            DiscreteActionFeatures(invalid_entries)
