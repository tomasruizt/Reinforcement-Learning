from typing import Dict

from rl.experience_tuple import ExperienceTuple


class ExperienceTupleSerializer:
    """A serializer for the ExperienceTuple class."""

    def serialize(self, experience_tuple: ExperienceTuple) -> Dict:
        """Serializes the input experience tuple in JSON format."""
        raise NotImplementedError
