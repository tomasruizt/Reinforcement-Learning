from rl.action import DiscreteAction, DiscreteActionScores


class DiscreteExplorator:
    """The Explorator has a built in exploration policy to help it decide
    what action to choose next."""

    def choose_action(self, action_scores: DiscreteActionScores) -> \
            DiscreteAction:
        """
        Chooses an action out of the scored actions.
        :param action_scores: An object containing the actions in the
        action space and their corresponding scores.
        :return: A single actions
        """
        raise NotImplementedError
