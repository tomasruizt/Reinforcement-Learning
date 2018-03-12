from typing import Iterable

from rl.action import DiscreteAction


class DiscreteState:
    """
    Simple State with a discrete state representation and a corresponding
    action space. This class in intended to be subclassed.
    """

    def __init__(self, action_space: Iterable[DiscreteAction]):
        """
        Initializes a state with the given action space.
        :param action_space: An iterable of actions that the agent can
        choose from.
        """
        self.action_space = action_space

    def is_final(self) -> bool:
        """Tells whether this state is final or not"""
        raise NotImplementedError
