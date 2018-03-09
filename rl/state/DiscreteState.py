from typing import Iterable

from rl.action import DiscreteAction


class DiscreteState:
    """
    Simple representation of a discrete state with a name and its corresponding action space.
    """

    def __init__(self, name: str, action_space: Iterable[DiscreteAction]):
        """
        Initializes a state with the given name and action space.
        :param name: The name of the state
        :param action_space: An iterable of actions that the agent can choose from.
        """
        self.name = name
        self.action_space = action_space
