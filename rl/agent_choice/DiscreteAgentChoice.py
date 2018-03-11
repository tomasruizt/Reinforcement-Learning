from rl.action import DiscreteAction
from rl.state import DiscreteState


class DiscreteAgentChoice:
    """
    A choice which described which state the Agent was in, and what Action it chose.
    """

    def __init__(self, from_state: DiscreteState, action_chosen: DiscreteAction):
        """
        Initialize the agents choice with the input state and chosen action.
        :param from_state: The state the agent was in whe it chose the action.
        :param action_chosen: The action the Agent chose when in the input state.
        """
        self.from_state = from_state
        self.action_chosen = action_chosen
