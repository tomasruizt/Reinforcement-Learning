from typing import Dict

from rl.episode import Episode
from rl.experience_tuple import ExperienceTupleSerializer


class EpisodeSerializer:
    """
    This serializer for Episode can be used in different
    scenarios by passing a specific implementation of an
    ExperienceTupleSerializer in the constructor.
    """

    def __init__(self,
                 experience_tuple_serializer: ExperienceTupleSerializer):
        """
        Initializes this class with a specific implementation of the
        experience tuple serializer.
        """
        assert experience_tuple_serializer is not None
        self._experience_tuple_serializer = experience_tuple_serializer

    def serialize(self, episode: Episode) -> Dict:
        """
        Serializes the input Episode into JSON format.
        :param episode: The Episode to serialize.
        :return: The serialized Episode.
        """
        assert episode is not None
        serialize = self._experience_tuple_serializer.serialize
        experience_tuples = [serialize(e) for e in episode.experience_tuples]
        return {
            "experienceTuples": experience_tuples
        }
