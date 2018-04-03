import unittest
from unittest.mock import MagicMock

from rl.agent import DiscreteAgent
from rl.environment import DiscreteEnvironment
from rl.episode import Episode
from rl.experience_tuple import ExperienceTuple
from rl.game import SequentialGame
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

    def test_play_one_episode_returns_one_episode(self):
        game = self._get_game_with_minimal_episodes()
        episode = game.play_one_episode()

        self.assertIsInstance(episode, Episode)

    def test_play_one_episode_calls_environment_get_initial_state(self):
        game = self._get_game_with_minimal_episodes()
        game.play_one_episode()
        game._environment.get_initial_state.assert_called_once()

    def test_play_one_episode_calls_environment_evaluate_agent_choice(self):
        game = self._get_game_with_minimal_episodes()
        game.play_one_episode()
        game._environment.evaluate_agent_choice.assert_called_once()

    def test_play_one_episode_calls_agent_choose_action(self):
        game = self._get_game_with_minimal_episodes()
        game.play_one_episode()
        game._agent.choose_action.assert_called_once()

    def test_play_one_episode_calls_agent_observe_experience_tuple(self):
        game = self._get_game_with_minimal_episodes()
        game.play_one_episode()
        game._agent.observe_experience_tuple.assert_called_once()

    def test_play_multiple_episodes_returns_multiple_episodes(self):
        expected_number_of_episodes = 4
        game = self._get_game_with_minimal_episodes()

        episodes = game.play_multiple_episodes(expected_number_of_episodes)
        self.assertEqual(expected_number_of_episodes, len(episodes))
        for episode in episodes:
            self.assertIsInstance(episode, Episode)

    # Auxiliary methods

    def _get_game_with_minimal_episodes(self):
        agent = MagicMock(spec=DiscreteAgent)
        environment = self._get_environment_with_minimal_episodes()
        game = SequentialGame(agent, environment)
        return game

    def _get_environment_with_minimal_episodes(self):
        environment = MagicMock(spec=DiscreteEnvironment)
        environment.get_initial_state.return_value = self._get_non_final_state()
        final_experience_tuple = \
            self._get_experience_tuple_with_final_end_state()
        environment.evaluate_agent_choice.return_value = final_experience_tuple
        return environment

    def _get_experience_tuple_with_final_end_state(self):
        final_experience_tuple = MagicMock(spec=ExperienceTuple)
        final_experience_tuple.end_state = self._get_final_state()
        return final_experience_tuple

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
