import numpy as np

from ActionSelector.ActionSelector import ActionSelector
from Interfaces import Estimator
from Policies.Policy import Policy


class BlackjackPolicy(Policy):

    def __init__(
            self,
            value_estimator: Estimator,
            action_selector: ActionSelector):
        self.estimator = value_estimator
        self.selector = action_selector

    def take_action(self, state):
        actions = ["settle", "draw_card"]
        value_estimates = [self.estimator.estimate(state, a) for a in actions]
        action_idx = self.selector.select_actions(value_estimates)
        return actions[action_idx]
