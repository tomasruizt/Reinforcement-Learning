from datasets import Writer

from rl.episode import EpisodeSerializer
from rl.experiment import ExperimentConfiguration
from rl.game import SequentialGame


class Experiment:
    """
    An experiment runs a game, parses its resulting episodes and saves
    the results to a folder.
    """

    def __init__(self, configuration: ExperimentConfiguration,
                 game: SequentialGame=None, writer: Writer=Writer()):
        """
        Initializes this class with the input configuration.
        :param configuration: The configuration of the experiment.
        """
        assert configuration is not None
        self._configuration = configuration
        self._game = game if game else self._get_new_game()
        self._writer = writer
        self._played_episodes = []
        self._serialized_episodes = []

    def run(self) -> None:
        """
        Runs the setup experiment.
        :return: None
        """
        self._reset_episodes()
        self._play_episodes()
        self._serialize_episodes()
        self._save_episodes_to_disk()

    # Private methods

    def _play_episodes(self):
        num_of_episodes = self._configuration.num_of_episodes
        self._played_episodes = \
            self._game.play_multiple_episodes(num_of_episodes)

    def _serialize_episodes(self):
        experience_tuple_serializer = \
            self._configuration.experience_tuple_serializer
        serializer = EpisodeSerializer(experience_tuple_serializer)
        self._serialized_episodes = \
            [serializer.serialize(episode) for episode in self._played_episodes]

    def _save_episodes_to_disk(self):
        basedir = self._configuration.results_directory
        self._writer.save_to_json_file(self._serialized_episodes, basedir)

    def _get_new_game(self):
        agent = self._configuration.agent
        environment = self._configuration.environment
        return SequentialGame(agent, environment)

    def _reset_episodes(self):
        self._played_episodes = []
        self._serialized_episodes = []
