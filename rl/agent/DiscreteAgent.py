from rl.agent_choice import DiscreteAgentChoice
from rl.experience_tuple import ExperienceTuple
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

    def observe_experience_tuple(self, experience_tuple: ExperienceTuple) -> \
            None:
        """
        Observes an ExperienceTuple to learn from it.
        :param experience_tuple: An object containing all the information
        necessary for learning algorithms.
        :return: None
        """
        raise NotImplementedError
