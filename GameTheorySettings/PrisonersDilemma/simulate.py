from Interfaces import Agent, Environment


def simulate(agent1: Agent, agent2: Agent, environment: Environment):
    LENGTH_OF_GAME = 5
    GAMES = 3

    total_history = []
    for _ in range(GAMES):
        state_initial = environment.get_initial_reward()
        action_available_initial = environment.get_initial_actions_available()
        reward_initial = environment.get_initial_reward()

        agent1.observe(state_initial, action_available_initial, reward_initial)
        agent2.observe(state_initial, action_available_initial, reward_initial)

        game_history = []
        for __ in range(LENGTH_OF_GAME):
            action_joint = agent1.take_action(), agent2.take_action()

            response = environment.get_response(action_joint, state_initial)
            reward1, reward2 = response.reward

            agent1.observe(response.state, response.actions_available, reward1)
            agent2.observe(response.state, response.actions_available, reward2)

            game_history.append((action_joint, response.reward))
        agent1.game_finished()
        agent2.game_finished()
        total_history.append(game_history)

    return total_history
