from Interfaces import GameFinished, Agent, Environment


def simulate(
        agent: Agent,
        environment: Environment,
        runs=200,
        iterations_per_run=200):

    results = []
    information = []
    for _ in range(runs):
        try:
            state_new, available_actions_new, reward = environment.get_initial_state_and_reward()
            for __ in range(iterations_per_run):
                agent.observe(state_new, available_actions_new, reward)
                state_current, action = agent.take_action()
                state_new, available_actions_new, reward = \
                    environment.get_new_state_and_reward(action, state_current)
        except GameFinished:
            pass
        results.append(agent.get_history())
        information.append(agent.get_information())
        agent.game_finished()
    return results, information
