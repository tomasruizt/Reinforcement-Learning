from rl.action import DiscreteAction
from rl.state import DiscreteState


class DiscreteAgentChoice:
    """
    A choice which described which state the Agent was in, and what Action it chose.
    """

    def __init__(self, state: DiscreteState, action_chosen: DiscreteAction):
        """
        Initialize the agents choice with the input state and chosen action.
        :param state: The state the agent was in.
        :param action_chosen: The action the Agent chose when in the input state.
        """
        self.state = state
        self.action_chosen = action_chosen
