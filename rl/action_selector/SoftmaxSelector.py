import numpy as np

from rl.action_selector.ActionSelector import ActionSelector


class SoftmaxSelector(ActionSelector):
    """
    This class uses a softmax function to select in a probabilistic way from the
    available actions.
    """
    def select_actions(self, action_value_estimates):
        probabilities = self.softmax(action_value_estimates)
        return np.random.choice(range(len(action_value_estimates)), p=probabilities)

    def softmax(self, x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()
