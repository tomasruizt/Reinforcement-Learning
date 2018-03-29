from typing import Iterable

from rl.agent import DiscreteAgent
from rl.environment import DiscreteEnvironment
from rl.game import DiscreteGameResult


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
        self._current_game_episodes = []
        self._current_state = None

    def play_once(self) -> DiscreteGameResult:
        """
        Makes the Agent play the Game once in the Environment.
        :return: The GameResult describing the single game played.
        """
        self._setup_new_game()
        while not self._current_state.is_final():
            self._move_to_next_state()
        return DiscreteGameResult(episodes=self._current_game_episodes)

    def play_multiple_times(self, times: int) -> Iterable[DiscreteGameResult]:
        """
        Makes the Agent play the Game multiple times in the Environment.
        :param times: Number of times to play the game.
        :return: A list of GameResults. Each GameResult describes the
        result of a single Game played.
        """
        assert times >= 1, "Input 'times' should be at least one."
        return [self.play_once() for _ in range(times)]

    def _setup_new_game(self):
        self._current_game_episodes = []
        self._current_state = self._environment.get_initial_state()

    def _move_to_next_state(self):
        """
        Makes the Agent move from the current state to the next state
        and logs the transition in current_game_episodes.
        :return: None
        """
        agent_choice = self._agent.choose_action(state=self._current_state)
        episode = self._environment.evaluate_agent_choice(agent_choice)
        self._agent.observe_episode(episode)

        self._log_episode(episode)
        self._current_state = episode.end_state

    def _log_episode(self, episode):
        self._current_game_episodes.append(episode)
