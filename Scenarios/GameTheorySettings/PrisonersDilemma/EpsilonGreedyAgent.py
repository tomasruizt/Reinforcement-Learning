from itertools import repeat

from Interfaces import Agent
from Policies.EpsilonGreedy import EpsilonGreedy

# TODO: Finish class

class EpsilonGreedyAgent(Agent):
    def __init__(self):
        self.policy = EpsilonGreedy(exploration_rate=repeat(0.5))
        self._actions_available_current = None
        self._history_states = []
        self._history_rewards = []

    def take_action(self):
        action_state_estimate_triplets = (
            self._actions_available_current,
            )
        return self.policy.select_action(action_state_estimate_triplets)

    def game_finished(self):
        pass

    def observe(self, state_new, actions_available_new, reward):
        self._actions_available_current = actions_available_new
        self._history_states.append(state_new)
        self._history_rewards.append(reward)

    def get_information(self):
        pass

    def get_history(self):
        pass
