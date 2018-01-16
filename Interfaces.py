class Environment:
    def get_new_state_and_reward(self, action, current_state):
        raise NotImplementedError

    def get_initial_state_and_reward(self):
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


class Estimator:
    def update_estimate(self, state_reward_pairs):
        raise NotImplementedError

    def estimate(self, key):
        raise NotImplementedError

    def get_information(self):
        raise NotImplementedError


class Policy:
    def select_action(self, action_state_estimate_triplets):
        """
        Selects an appropate action to take.
        :param action_state_estimate_triplets: triplets of the form
        (action, new_state, estimate) for the policy to choose from.
        :return: pair (idx, new_estimation)
        """
        raise NotImplemented
