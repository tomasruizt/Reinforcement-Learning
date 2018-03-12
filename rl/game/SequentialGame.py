from typing import Iterable

from rl.agent import DiscreteAgent
from rl.environment import DiscreteEnvironment
from rl.episode import DiscreteEpisode
from rl.state import DiscreteState


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
        self._agent = agent
        self._environment = environment

    def run_once(self) -> Iterable[DiscreteEpisode]:
        """
        Runs the game once between the Agent and the Environment.
        :return: The sequence of episodes that describe the sequential
        game just run.
        """
        episode_sequence = []
        state = self._environment.get_initial_state()
        while not state.is_final():
            episode = self._agent_makes_a_choice(from_state=state)
            episode_sequence.append(episode)
            state = episode.end_state
        return episode_sequence

    def _agent_makes_a_choice(self, from_state: DiscreteState) -> \
            DiscreteEpisode:
        """
        Makes the Agent take a single choice and return an episode that
        describes the interaction with the environment.
        :param from_state: The state from which the Agent will make a
        choice.
        :return: The Episode describing the Agent-Environment interaction.
        """
        agent_choice = self._agent.choose_action(from_state)
        episode = self._environment.evaluate_agent_choice(agent_choice)
        self._agent.observe_episode(episode)
        return episode
