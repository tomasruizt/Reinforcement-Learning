from rl.agent import DiscreteAgent
from rl.environment import DiscreteEnvironment
from rl.experience_tuple import ExperienceTupleSerializer


class ExperimentConfiguration:
    """Configuration to run an Experiment."""

    def __init__(self, agent: DiscreteAgent, environment: DiscreteEnvironment,
                 num_of_episodes: int, results_directory: str,
                 experience_tuple_serializer: ExperienceTupleSerializer):

        self._validate_input(agent, environment, num_of_episodes,
                             results_directory, experience_tuple_serializer)

        self.results_directory = results_directory
        self.environment = environment
        self.num_of_episodes = num_of_episodes
        self.agent = agent
        self.experience_tuple_serializer = experience_tuple_serializer

    @staticmethod
    def _validate_input(agent, environment, num_of_episodes,
                        results_directory, experience_tuple_serializer):
        assert agent is not None
        assert environment is not None
        assert num_of_episodes is not None
        assert results_directory is not None
        assert experience_tuple_serializer is not None
