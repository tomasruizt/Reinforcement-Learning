from typing import List

import numpy
from rl.action import DiscreteAction


class DiscreteActionFeatures(dict):
    """
    A dict-like class that assigns a featurized representation to
    every action. Keys are actions and values are numpy arrays
    """

    def values(self) -> List[numpy.ndarray]:
        return list(super().values())

    def features_dimension(self) -> int:
        any_action_features = next(iter(self.values()))
        return len(any_action_features)

    def __getitem__(self, k: DiscreteAction) -> numpy.ndarray:
        assert isinstance(k, DiscreteAction)
        return super().__getitem__(k)

    def __setitem__(self, key, value):
        raise NotImplementedError("Its not allowed to modify the action "
                                  "features.")

    def __init__(self, *args, **kwargs):
        """
        All the keys should be of type 'DiscreteAction'" and all the
        values should 'numpy.ndarray' of the same length.
        """
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            assert isinstance(key, DiscreteAction)
            assert isinstance(value, numpy.ndarray)
        feature_lengths = [len(val) for val in self.values()]
        assert max(feature_lengths) == min(feature_lengths)
