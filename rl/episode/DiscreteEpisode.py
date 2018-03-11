from rl.action import DiscreteAction
from rl.state import DiscreteState


class DiscreteEpisode:
    """
    An episode describes a full interaction of the Agent and the Environment. It contains all the information required
    by learning algorithms. It has a starting state, the Agent's action, the corresponding reward and the end state the
    action lead the Agent to. This Episode works with discrete states
    and actions.
    """

    def __init__(self, start_state: DiscreteState, agent_action: DiscreteAction, reward: float,
                 end_state: DiscreteState):
        """
        Initializes a DiscreteEpisode with the given input.
        :param start_state: The starting state from which the Agent chose an action from.
        :param agent_action: The action the Agent chose.
        :param reward: The reward received for transitioning from state start_state to end_state.
        :param end_state: The sate where the Agent transitioned to by taking the action_chosen.
        """
        self.start_state = start_state
        self.agent_action = agent_action
        self.reward = reward
        self.end_state = end_state

