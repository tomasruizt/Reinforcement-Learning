from Interfaces import Estimator, Policy
from Setting10x10.TenTimesTenAgent import TenTimesTenAgent


class ModularAgent(TenTimesTenAgent):
    def __init__(
            self,
            estimator: Estimator,
            policy: Policy,
            value_update_rate="per_game"
    ):
        assert (value_update_rate in ["per_game", "per_step"])
        self._update_method = \
            "observe" if value_update_rate == "per_step" else "game_finished"
        self._learn_rate = value_update_rate
        self._estimator = estimator
        self._policy = policy
        super().__init__()

    def take_action(self):
        states = self._get_states_neighboring()
        estimates = [self._estimator.estimate(state) for state in states]
        idx, estimate = self._policy.select_action(
            list(zip(self._actions_available_current, states, estimates)))
        action = self._actions_available_current[idx]
        self._log_action(action, estimate)
        return self._state_current(), action

    def observe(self, state_new, actions_available_new, reward):
        super().observe(state_new, actions_available_new, reward)
        self._update_estimator(caller_method="observe")

    def get_information(self):
        return self._estimator.get_information()

    def game_finished(self):
        self._update_estimator(caller_method="game_finished")
        super().game_finished()

    def _update_estimator(self, caller_method):
        if caller_method == self._update_method:
            state_reward_pairs = zip(self._history_states, self._history_rewards)
            self._estimator.update_estimate(state_reward_pairs)
