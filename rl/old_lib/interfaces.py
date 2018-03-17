"""
This is the module docstring
"""


class EnvironmentResponse:
    """
    This is a docstring
    """
    def __init__(self, state, actions_available, reward):
        self.state = state
        self.actions_available = actions_available
        self.reward = reward


class Environment:
    """The environment"""
    def get_response(self, action, current_state) -> EnvironmentResponse:
        """
        More docstring
        :param action:
        :param current_state:
        :return:
        """
        raise NotImplementedError

    def get_initial_state(self):
        """
        MOre docstring
        :return:
        """
        raise NotImplementedError


class GameFinished(Exception):
    """Docstring stuff"""
    pass


class Policy:
    """This is a policy"""
    def select_action(self, action_state_estimate_triplets):
        """
        Selects an appropriate action to take.
        :param action_state_estimate_triplets: triplets of the form
        (action, new_state, estimate) for the policy to choose from.
        :return: pair (idx, new_estimation)
        """
        raise NotImplementedError
