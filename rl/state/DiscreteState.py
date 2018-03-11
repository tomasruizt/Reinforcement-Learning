from typing import Iterable

from rl.action import DiscreteAction


class DiscreteState:
    """
    Simple State with a discrete state representation and its corresponding action space.
    """

    def __init__(self, representation, action_space: Iterable[DiscreteAction]):
        """
        Initializes a state with the given name and action space.
        :param representation: Discrete representation of the state.
        :param action_space: An iterable of actions that the agent can choose from.
        """
        self.representation = representation
        self.action_space = action_space
