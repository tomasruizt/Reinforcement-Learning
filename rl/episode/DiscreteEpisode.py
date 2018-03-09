from rl.action import DiscreteAction
from rl.state import DiscreteState


class DiscreteEpisode:
    """
    An episode describes a full interaction of the Agent and the Environment. This Episode works with discrete states
    and actions.
    """

    def __init__(self, start_state: DiscreteState, action_chosen: DiscreteAction, reward: float,
                 end_state: DiscreteState):
        """
        Initializes a DiscreteEpisode with the given input.
        :param start_state: The starting state from which the Agent chose an action from.
        :param action_chosen: The action the Agent chose.
        :param reward: The reward received for transitioning from state start_state to end_state.
        :param end_state: The sate where the Agent transitioned to by taking the action_chosen.
        """
        self.start_state = start_state
        self.action_chosen = action_chosen
        self.reward = reward
        self.end_state = end_state

