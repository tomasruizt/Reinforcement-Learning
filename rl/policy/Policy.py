from rl.policy.ActionDistribution import ActionDistribution


class Policy:
    """
    Selects an appropriate action.
    """
    def get_action_distribution(self, state, action_space) -> ActionDistribution:
        """
        Chooses one or several actions in the given action space, given an input state.
        :param state: The environment state.
        :param action_space: The current action space to select take actions from.
        :return: A probability distribution over the actions
        """
        raise NotImplementedError
