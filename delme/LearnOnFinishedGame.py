from Interfaces import Estimator, Policy
from Setting10x10.TenTimesTenAgent import TenTimesTenAgent


class LearnOnFinishedGame(TenTimesTenAgent):
    def __init__(self, state, actions_available, estimator: Estimator, policy: Policy):
        self._estimator = estimator
        self._policy = policy
        super().__init__(state, actions_available)

    def take_action(self):
        estimates = [self._estimator.estimate(state) for state in
                     self._get_states_neighboring()]
        idx, estimate = self._policy.select_action(estimates)
        action_selected = self._actions_available_current[idx]
        self._log_action(action_selected, estimate)
        return self._state_current, action_selected

    def game_finished(self):
        self._estimator.update_estimate(self._history_states_and_rewards)
        super().game_finished()

    def get_information(self):
        return self._estimator.get_information()
