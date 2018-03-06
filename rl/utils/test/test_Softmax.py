import unittest

import math
from numpy import random

from rl.utils.Softmax import softmax


class SoftmaxTest(unittest.TestCase):

    def setUp(self):
        self.PRECISION = 1e-10

    def test_softmax_on_list(self):
        softmax_input = random.uniform(-100, 100, 10)
        softmax_expected_output = self.create_softmax_expected_output(softmax_input)

        actual_output = softmax(softmax_input)
        for actual, expected in zip(actual_output, softmax_expected_output):
            self.assertAlmostEqual(actual, expected, delta=self.PRECISION)

    @staticmethod
    def create_softmax_expected_output(collection):
        input_potentiated = [math.e ** i for i in collection]
        denominator = sum(input_potentiated)
        return [i / denominator for i in input_potentiated]
