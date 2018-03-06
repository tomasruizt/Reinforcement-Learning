from rl.value_approximator.StateActionValues import StateActionValues


class ValueApproximator:
    """
    A function to approximate the value of a state-action pair. The function can update its approximation when it
    observes the reward of its actions.
    """

    def approximate_value(self, state, actions) -> StateActionValues:
        """
        Approximates the value of the state paired with every action in actions.
        :param state: The current state.
        :param actions: A list of strings referring to the actions.
        :return: An object containing the value approximations for every state-action pair.
        """
        raise NotImplementedError

    def update_approximation(self, start_state, start_action, reward, end_state, end_action):
        """
        Uses an past interaction with the environment to update its value approximation function.
        The interaction is encoded in SARSA style (State, Action, Reward, State', Action').
        :param start_state: The state from which the agent took the action start_action.
        :param start_action: The action taken by the agent in state start_state.
        :param reward: The reward observed by transitioning from state start_state to state end_state.
        :param end_state: The state the agent landed on after taking action start_action.
        :param end_action: The action that corresponds to the highest value state-action pair in state end_state.
        :return: None
        """
        raise NotImplementedError
