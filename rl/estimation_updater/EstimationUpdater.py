# TODO: An estimation updater should not offer the estimate() API, neither the get_information() one.
class EstimationUpdater:
    def update_estimate(self, state_reward_pairs):
        raise NotImplementedError

    def estimate(self, state, action=None):
        raise NotImplementedError

    def get_information(self):
        raise NotImplementedError