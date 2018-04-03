from typing import Sequence

from rl.experience_tuple import ExperienceTuple


class Episode:
    """
    The Episode is a sequence of ExperienceTuples that protocol a
    single run of a Game.
    """

    def __init__(self, experience_tuples: Sequence[ExperienceTuple]):
        """Initialize the Episode with the input experience tuples."""
        self._validate_input(experience_tuples)
        self.experience_tuples = experience_tuples

    @staticmethod
    def _validate_input(experience_tuples: Sequence[ExperienceTuple]):
        """Validate that the input has at least one ExperienceTuple."""
        assert experience_tuples is not None
        assert len(experience_tuples) >= 1, "Input 'experience_tuples' " \
                                            "should have at least one element."
        for experience_tuple in experience_tuples:
            assert isinstance(experience_tuple, ExperienceTuple),\
                "Input 'experience_tuples' should contain only " \
                "ExperienceTuple, but contains: '%s'." % experience_tuple
