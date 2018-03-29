import unittest
from unittest.mock import MagicMock

from rl.agent import DiscreteAgent
from rl.environment import DiscreteEnvironment
from rl.episode import DiscreteEpisode
from rl.game import SequentialGame, DiscreteGameResult
from rl.state import DiscreteState


class SequentialGameTest(unittest.TestCase):

    def test_constructor_reject_none_input_agent(self):
        expected_regex = "Constructor input 'agent' should not be None."
        with self.assertRaisesRegex(AssertionError, expected_regex):
            SequentialGame(agent=None, environment=MagicMock())

    def test_constructor_reject_none_input_environment(self):
        expected_regex = "Constructor input 'environment' should not be None."
        with self.assertRaisesRegex(AssertionError, expected_regex):
            SequentialGame(agent=MagicMock(), environment=None)

    def test_play_once_returns_one_game_result(self):
        game = self._get_game_with_single_episode()
        game_result = game.play_once()

        self.assertIsInstance(game_result, DiscreteGameResult)

    def test_play_once_calls_environment_get_initial_state(self):
        game = self._get_game_with_single_episode()
        game.play_once()
        game._environment.get_initial_state.assert_called_once()

    def test_play_once_calls_environment_evaluate_agent_choice(self):
        game = self._get_game_with_single_episode()
        game.play_once()
        game._environment.evaluate_agent_choice.assert_called_once()

    def test_play_once_calls_agent_choose_action(self):
        game = self._get_game_with_single_episode()
        game.play_once()
        game._agent.choose_action.assert_called_once()

    def test_play_once_calls_agent_observe_episode(self):
        game = self._get_game_with_single_episode()
        game.play_once()
        game._agent.observe_episode.assert_called_once()

    def test_play_multiple_times_returns_multiple_game_results(self):
        expected_game_results = 4
        game = self._get_game_with_single_episode()

        games_results = game.play_multiple_times(expected_game_results)
        self.assertEqual(expected_game_results, len(games_results))
        for game_result in games_results:
            self.assertIsInstance(game_result, DiscreteGameResult)

    # Auxiliary methods

    def _get_game_with_single_episode(self):
        agent = MagicMock(spec=DiscreteAgent)
        environment = self._get_environment_with_a_single_episode()
        game = SequentialGame(agent, environment)
        return game

    def _get_environment_with_a_single_episode(self):
        environment = MagicMock(spec=DiscreteEnvironment)
        environment.get_initial_state.return_value = self._get_non_final_state()
        final_episode = self._get_episode_with_final_end_state()
        environment.evaluate_agent_choice.return_value = final_episode
        return environment

    def _get_episode_with_final_end_state(self):
        non_final_episode = MagicMock(spec=DiscreteEpisode)
        non_final_episode.end_state = self._get_final_state()
        return non_final_episode

    @staticmethod
    def _get_non_final_state():
        non_final_state = MagicMock(spec=DiscreteState)
        non_final_state.is_final.return_value = False
        return non_final_state

    @staticmethod
    def _get_final_state():
        final_state = MagicMock(spec=DiscreteState)
        final_state.is_final.return_value = True
        return final_state
