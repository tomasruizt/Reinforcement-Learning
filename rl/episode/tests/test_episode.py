import unittest

from rl.episode import Episode


class EpisodeTest(unittest.TestCase):

    def test_validation_none_rejected(self):
        with self.assertRaises(AssertionError):
            Episode(experience_tuples=None)

    def test_validation_input_len_greater_equal_one(self):
        expected_regex = "Input 'experience_tuples' should have at least one " \
                         "element."
        with self.assertRaisesRegex(AssertionError, expected_regex):
            Episode(experience_tuples=[])

    def test_validation_input_are_not_experience_tuples(self):
        expected_regex = "Input 'experience_tuples' should contain only " \
                         "ExperienceTuple, but contains: '1'."
        with self.assertRaisesRegex(AssertionError, expected_regex):
            Episode(experience_tuples=[1, 2, 3])
