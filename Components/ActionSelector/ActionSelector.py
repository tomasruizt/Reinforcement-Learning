class ActionSelector:
    """
    The selector is a component of the policy and is responsible to select one
    or more actions based on the passed scores. It enables probabilistic treatment
    of the scores.
    """
    def select_actions(self, action_value_estimates):
        raise NotImplementedError
