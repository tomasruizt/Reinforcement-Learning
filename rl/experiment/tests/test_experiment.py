import unittest
from unittest.mock import MagicMock

from rl.episode import Episode
from rl.experience_tuple import ExperienceTuple
from rl.experiment import Experiment


class ExperimentTest(unittest.TestCase):

    def test_constructor_rejects_none_configuration(self):
        with self.assertRaises(AssertionError):
            Experiment(configuration=None)

    @staticmethod
    def test_run_calls_game_with_configured_num_of_episodes():
        num_of_episodes = 3
        configuration = MagicMock()
        configuration.num_of_episodes = num_of_episodes
        game = MagicMock()

        Experiment(configuration, game, writer=MagicMock()).run()
        game.play_multiple_episodes.assert_called_with(num_of_episodes)

    def test_run_calls_experience_tuple_serializer(self):
        configuration = \
            self._setup_configuration_with_experience_tuple_serializer()
        game = MagicMock()
        experience_tuple = self._get_expected_experience_tuple(game)

        Experiment(configuration, game=game, writer=MagicMock()).run()
        configuration.experience_tuple_serializer.serialize.assert_called_with(
            experience_tuple)

    @staticmethod
    def test_run_calls_file_writer_as_configured():
        configuration = MagicMock()
        results_directory = "placeholder"
        configuration.results_directory = results_directory
        writer = MagicMock()

        Experiment(configuration, game=MagicMock(), writer=writer).run()
        writer.save_to_json_file.assert_called_with([], results_directory)

    # Auxiliary methods

    @staticmethod
    def _get_expected_experience_tuple(game):
        experience_tuple = MagicMock(spec=ExperienceTuple)
        episodes = [Episode([experience_tuple])]
        game.play_multiple_episodes.return_value = episodes
        return experience_tuple

    @staticmethod
    def _setup_configuration_with_experience_tuple_serializer():
        experience_tuple_serializer = MagicMock()
        configuration = MagicMock()
        configuration.experience_tuple_serializer = experience_tuple_serializer
        return configuration
