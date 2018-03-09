from rl.agent_choice import DiscreteAgentChoice
from rl.episode import DiscreteEpisode
from rl.state import DiscreteState


class DiscreteAgent:
    """
    Simple agent that works with discrete actions and states.
    """

    def choose_action(self, state: DiscreteState) -> DiscreteAgentChoice:
        """
        Given an input state, chooses an action.
        :param state: The input state.
        :return: A DiscreteAgentChoice with the input state and the chosen action.
        """
        raise NotImplementedError

    def observe_episode(self, episode: DiscreteEpisode):
        """
        Observes an Episode to learn from it.
        :param episode: The episode with all the necessary information.
        :return: None
        """
        raise NotImplementedError
