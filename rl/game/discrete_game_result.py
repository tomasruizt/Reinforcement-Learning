from typing import Iterable

from rl.episode import DiscreteEpisode


class DiscreteGameResult:
    """
    The GameResult is a collection of Episodes that protocol the a
    single run of a Game.
    """

    def __init__(self, episodes: Iterable[DiscreteEpisode]):
        """Initialize the GameResult with the input episodes."""
        self._validate_input(episodes)
        self.episodes = episodes

    @staticmethod
    def _validate_input(episodes: Iterable[DiscreteEpisode]):
        """Validate that the input is not empty"""
        assert episodes is not None, "Input should not be None."
        assert len(episodes) >= 1, "Input 'episodes' should have at least " \
                                   "one element."
        for episode in episodes:
            assert isinstance(episode, DiscreteEpisode), "Input 'episodes' " \
                "should contain only episodes, but contains: '%s'." % episode
