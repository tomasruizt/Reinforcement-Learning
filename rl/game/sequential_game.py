from typing import List

from rl.agent import DiscreteAgent
from rl.environment import DiscreteEnvironment
from rl.episode import Episode
from rl.experience_tuple import ExperienceTuple


class SequentialGame:
    """
    Game where the agent takes decisions sequentially. At every step,
    the Agents see the Environment state it is located in, chooses an
    action and transitions to a new state of the Environment. The
    Environment  rewards the Agent's action with some scalar value. This
    process is repeated until the Agent reaches a terminal state of the
    Environment.
    """

    def __init__(self, agent: DiscreteAgent, environment: DiscreteEnvironment):
        """
        Setups a sequential Game for the input Agent in the input
        Environment.
        :param agent: The Agent that will take sequential decisions.
        :param environment: The Environment where the Agent will take
        decisions.
        """
        assert agent is not None, "Constructor input 'agent' should not be " \
                                  "None."
        assert environment is not None, "Constructor input 'environment' " \
                                        "should not be None."
        self._agent = agent
        self._environment = environment
        self._current_episodes_experience_tuples = []
        self._current_state = None

    def play_one_episode(self) -> Episode:
        """
        Makes the Agent play a single Episode in the Environment.
        :return: The single Episode played.
        """
        self._setup_new_episode()
        while not self._current_state.is_final():
            self._move_to_next_state()
        return Episode(self._current_episodes_experience_tuples)

    def play_multiple_episodes(self, number_of_episodes: int) -> List[Episode]:
        """
        Makes the Agent play multiple Episodes in the Environment.
        :param number_of_episodes: Number of Episodes to play.
        :return: A list of the played Episodes.
        """
        assert number_of_episodes >= 1, "Input 'number_of_episodes' should " \
                                        "be at least one."
        return [self.play_one_episode() for _ in range(number_of_episodes)]

    def _setup_new_episode(self):
        self._current_episodes_experience_tuples = []
        self._current_state = self._environment.get_initial_state()

    def _move_to_next_state(self):
        """
        Makes the Agent move from the current state to the next state
        and logs the transition.
        :return: None
        """
        agent_choice = self._agent.choose_action(state=self._current_state)
        experience_tuple = self._environment.evaluate_agent_choice(agent_choice)
        self._agent.observe_experience_tuple(experience_tuple)

        self._log_experience_tuple(experience_tuple)
        self._current_state = experience_tuple.end_state

    def _log_experience_tuple(self, experience_tuple: ExperienceTuple):
        self._current_episodes_experience_tuples.append(experience_tuple)
