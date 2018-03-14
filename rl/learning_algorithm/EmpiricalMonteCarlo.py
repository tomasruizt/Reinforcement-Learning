class MonteCarlo(ContextFreeValueApproximator):
    def __init__(self, update_rule: UpdateRule=DifferentialUpdate(), initial_value_estimate=0):
        self._state_action_values = defaultdict(lambda: initial_value_estimate)

    def approximate_value(self, state: str, actions: str) -> StateActionValues:
        state_action_pairs = [(state, action) for action in actions]
        values = np.array(self._state_action_values[pair] for pair in state_action_pairs)
        return StateActionValues(state_action_pairs, values)

    def update_approximation(
            self, start_state: str, start_action: str, reward: float, end_state: str, end_action: str):


    def update_estimate(self, state_reward_pairs):
        states, rewards = zip(*state_reward_pairs)
        mc_value_estimations = np.flip(np.cumsum(np.flip(rewards, 0)), 0)
        # Update estimation, using running average
        for state, mc_value_estimation in zip(states, mc_value_estimations):
            self._state_action_values[state] = self._update_rule.get_new_estimate(
                key=state,
                estimate_old=self._state_action_values[state],
                estimate_sample=mc_value_estimation)

    def estimate(self, state):
        return self._state_action_values[state]

    def get_information(self):
        return self._state_action_values.copy()
