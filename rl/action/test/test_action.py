import unittest

from rl.action.DiscreteAction import DiscreteAction


class ActionTest(unittest.TestCase):

    def test_constructor_rejects_non_string_name(self):
        name = 100
        with self.assertRaisesRegex(AssertionError, "Input 'name' should be a string but is '%s'" % str(type(name))):
            DiscreteAction(name)
