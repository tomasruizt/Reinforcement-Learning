from rl.action import DiscreteAction
from rl.state import DiscreteState


class ExperienceTuple:
    """
    An experience tuple describes a single interaction of the Agent and
    the Environment. It contains all the information required by learning
    algorithms. It has a starting state, the Agent's action, the
    corresponding reward and the Agent's end state.
    This experience tuple works with discrete states and actions.
    """

    def __init__(self, start_state: DiscreteState, agent_action: DiscreteAction,
                 reward: float, end_state: DiscreteState):
        """
        Initializes an ExperienceTuple with the given input.
        :param start_state: The starting state from which the Agent
        chose an action from.
        :param agent_action: The action the Agent chose.
        :param reward: The reward received for transitioning from state
        start_state to end_state.
        :param end_state: The sate where the Agent transitioned to by
        taking the action_chosen.
        """
        self._validate_input(start_state, agent_action, reward, end_state)
        self.start_state = start_state
        self.agent_action = agent_action
        self.reward = reward
        self.end_state = end_state

    @staticmethod
    def _validate_input(start_state, agent_action, reward, end_state):
        error_message = "Input '%s' should not be None."
        assert start_state is not None, error_message % "start_state"
        assert agent_action is not None, error_message % "agent_action"
        assert reward is not None, error_message % "reward"
        assert end_state is not None, error_message % "end_state"

