from itertools import zip_longest

from Interfaces import Agent


class TenTimesTenAgent(Agent):

    def __init__(self):
        self._actions_deltas = {
            "right": (1, 0),
            "up": (0, 1),
            "left": (-1, 0),
            "down": (0, -1)
        }

        self._history_states = []
        self._history_rewards = []
        self._history_actions = []
        self._history_actions_estimates = []

        self._actions_available_current = None

    def observe(self, state_new, actions_available_new, reward):
        self._actions_available_current = actions_available_new
        self._history_states.append(state_new)
        self._history_rewards.append(reward)

    def game_finished(self):
        self._history_states = []
        self._history_rewards = []
        self._history_actions = []
        self._history_actions_estimates = []

        self._actions_available_current = None

    def get_history(self):
        return list(zip_longest(
            self._history_rewards,
            self._history_states,
            self._history_actions,
            self._history_actions_estimates))

    def _get_states_neighboring(self):
        states_neighboring = []
        for action in self._actions_available_current:
            dx = self._actions_deltas[action]
            state_current = self._state_current()
            neighbor = (state_current[0] + dx[0], state_current[1] + dx[1])
            states_neighboring.append(neighbor)
        return states_neighboring

    def _log_action(self, action, estimate):
        self._history_actions.append(action)
        self._history_actions_estimates.append(estimate)

    def take_action(self):
        raise NotImplementedError

    def get_information(self):
        raise NotImplementedError

    def _state_current(self):
        return self._history_states[-1] if len(self._history_states) > 0 else None
