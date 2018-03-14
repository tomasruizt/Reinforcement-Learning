import unittest

import numpy

from rl.value_approximator.StateActionValues import StateActionValues


class StateActionValuesTest(unittest.TestCase):

    def test_constructor_rejects_invalid_input(self):
        """
        The constructor shall reject the input when the parameters don't have the same length.
        :return: None
        """
        state_actions = ["one", "two"]
        too_many_values = numpy.array([1, 2, 3])
        too_few_values = numpy.array([1])

        expected_msg_fragment = "Length of input"
        with self.assertRaisesRegex(AssertionError, expected_msg_fragment):
            StateActionValues(state_actions, too_many_values)

        with self.assertRaisesRegex(AssertionError, expected_msg_fragment):
            StateActionValues(state_actions, too_few_values)
