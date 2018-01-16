from collections import defaultdict
from itertools import repeat


class UpdateRule:
    def get_new_estimate(self, key, estimate_old, estimate_sample):
        raise NotImplementedError


class RunningAverage(UpdateRule):
    def __init__(self):
        self._visited = defaultdict(int)

    def get_new_estimate(self, key, estimate_old, estimate_sample):
        n = self._visited[key]
        total_sum = estimate_old * n
        total_sum_new = total_sum + estimate_sample
        self._visited[key] += 1
        estimation_new = total_sum_new / self._visited[key]
        return estimation_new


class DifferentialUpdate(UpdateRule):
    def __init__(self, learning_rate=repeat(0.05)):
        self._learning_rate = learning_rate

    def get_new_estimate(self, key, estimate_old, estimate_sample):
        learning_rate = next(self._learning_rate)
        difference = estimate_sample - estimate_old
        return estimate_old + learning_rate * difference

