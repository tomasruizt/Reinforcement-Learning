from typing import Optional, List

import numpy as np
from collections import defaultdict
from rl.episode import DiscreteEpisode
from rl.featurizer import DiscreteFeaturizer
from rl.learning_algorithm import LearningAlgorithm
from rl.regressor import FittingData


class MonteCarlo(LearningAlgorithm):
    def __init__(self, featurizer: DiscreteFeaturizer):
        self._featurizer = featurizer
        self._unbiased_estimation = defaultdict(int)
        self._current_game = []  # List[Episode]

    def observe(self, episode: DiscreteEpisode) -> Optional[FittingData]:
        self._current_game.append(episode)
        if episode.end_state.is_final():
            self._update_unbiased_estimation_with(self._current_game)
            return self._return_fitting_data()
        else:
            return None

    # Private methods

    def _return_fitting_data(self):
        pass

    def update_estimate(self, state_reward_pairs):
        states, rewards = zip(*state_reward_pairs)
        mc_value_estimations = np.flip(np.cumsum(np.flip(rewards, 0)), 0)
        # Update estimation, using running average
        for state, mc_value_estimation in zip(states, mc_value_estimations):
            self._state_action_values[state] = self._update_rule.get_new_estimate(
                key=state,
                estimate_old=self._state_action_values[state],
                estimate_sample=mc_value_estimation)

    def _update_unbiased_estimation_with(
            self, current_game: List[DiscreteEpisode]):
        start_states = [episode.start_state for episode in current_game]
        actions = [episode for episode in current_game]
        rewards = [episode.__getattribute__() for episode in current_game]


