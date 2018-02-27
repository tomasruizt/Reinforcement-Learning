from numpy import random

from Scenarios.Setting10x10.TenTimesTenAgent import TenTimesTenAgent


class RandomAgent(TenTimesTenAgent):
    def take_action(self):
        action = random.choice(self._actions_available_current)
        self._history_actions.append(action)
        return self._state_current, action

    def get_information(self):
        pass
