import numbers
from typing import List

from rl.action import DiscreteAction


class DiscreteActionScores(dict):
    """
    Container class that assigns a float score for every action.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for action, score in self.items():
            assert isinstance(action, DiscreteAction)
            assert isinstance(score, numbers.Real)  # Accepts both int and float

    def values(self) -> List[float]:
        return list(super().values())

    def __getitem__(self, k: DiscreteAction) -> float:
        assert isinstance(k, DiscreteAction)
        return super().__getitem__(k)

    def __setitem__(self, key, value):
        raise NotImplementedError("Its not allowed to modify the action "
                                  "scores.")
