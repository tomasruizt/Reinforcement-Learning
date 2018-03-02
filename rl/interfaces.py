class EnvironmentResponse:
    def __init__(self, state, actions_available, reward):
        self.state = state
        self.actions_available = actions_available
        self.reward = reward


class Environment:
    def get_response(self, action, current_state) -> EnvironmentResponse:
        raise NotImplementedError

    def get_initial_state(self):
        raise NotImplementedError

    def get_initial_actions_available(self):
        raise NotImplementedError

    def get_initial_reward(self):
        raise NotImplementedError


class GameFinished(Exception):
    pass


class Agent:
    def take_action(self):
        raise NotImplementedError

    def observe(self, state_new, actions_available_new, reward):
        raise NotImplementedError

    def game_finished(self):
        raise NotImplementedError

    def get_history(self):
        raise NotImplementedError

    def get_information(self):
        raise NotImplementedError


class Policy:
    def select_action(self, action_state_estimate_triplets):
        """
        Selects an appropriate action to take.
        :param action_state_estimate_triplets: triplets of the form
        (action, new_state, estimate) for the policy to choose from.
        :return: pair (idx, new_estimation)
        """
        raise NotImplemented

