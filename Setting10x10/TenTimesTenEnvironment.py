from Interfaces import Environment, GameFinished


class TenTimesTenEnvironment(Environment):

    def __init__(self, reward_function):
        self._reward_function = reward_function
        self._state_initial = (0, 0)
        self._state_final = (9, 9)
        self._actions_deltas = {
            "right": (1, 0),
            "up": (0, 1),
            "left": (-1, 0),
            "down": (0, -1)
        }
        self._states = {(x1, x2) for x1 in range(10) for x2 in range(10)}
        self._actions_available = \
            {state: self._generate_available_actions(state) for state in self._states}

    def _generate_available_actions(self, state):
        actions_available = []
        for action, dx in self._actions_deltas.items():
            if (state[0] + dx[0], state[1] + dx[1]) in self._states:
                actions_available.append(action)
        return actions_available

    def get_response(self, action_taken, state_current):
        if state_current == self._state_final:
            raise GameFinished

        dx = self._actions_deltas[action_taken]
        state_new = (state_current[0] + dx[0], state_current[1] + dx[1])

        if state_new not in self._states:
            raise Exception("Invalid action")

        actions_available_new = self._actions_available[state_new]
        reward = self._reward_function(state_new[0], state_new[1])

        return state_new, actions_available_new, reward

    def get_initial_state(self):
        return self._state_initial

    def get_initial_actions_available(self):
        return self._actions_available[self._state_initial]

    def get_initial_reward(self):
        return 0
