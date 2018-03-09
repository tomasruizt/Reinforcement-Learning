from rl.agent_choice import DiscreteAgentChoice
from rl.episode import DiscreteEpisode
from rl.state import DiscreteState


class DiscreteEnvironment:
    """
    The environment interacts with the agent and evaluates its choices. This environment works with discrete states
    and actions.
    """

    def get_initial_state(self) -> DiscreteState:
        """
        Retrieve an initial State, for the Agent to begin interacting.
        :return: The initial state.
        """
        raise NotImplementedError

    def evaluate_agent_choice(self, choice: DiscreteAgentChoice) -> DiscreteEpisode:
        """
        Evaluates the agent's choice and return an Episode describing the entire interaction.
        :param choice: The agent's choice.
        :return: The episode with the interaction.
        """
        raise NotImplementedError
