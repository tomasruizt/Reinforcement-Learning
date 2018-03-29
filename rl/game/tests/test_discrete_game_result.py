import unittest

from rl.game import DiscreteGameResult


class DiscreteGameResultTest(unittest.TestCase):

    def test_validation_none_rejected(self):
        expected_regex = "Input should not be None."
        with self.assertRaisesRegex(AssertionError, expected_regex):
            DiscreteGameResult(episodes=None)

    def test_validation_input_len_greater_equal_one(self):
        expected_regex = "Input 'episodes' should have at least one element."
        with self.assertRaisesRegex(AssertionError, expected_regex):
            DiscreteGameResult(episodes=[])

    def test_validation_input_are_not_episodes(self):
        expected_regex = "Input 'episodes' should contain only episodes, but " \
                         "contains: '1'."
        with self.assertRaisesRegex(AssertionError, expected_regex):
            DiscreteGameResult(episodes=[1, 2, 3])
