from Components.Agents.ModularAgent import ModularAgent
from Components.Estimators.MonteCarlo import MonteCarlo
from Components.Estimators.TDLambda import TDLambda
from Components.Policies.EpsilonGreedy import EpsilonGreedy
from Components.Policies.UCB import UCB
from Components.RL_utils.LearningRate import linear_decay, step_function

from Scenarios.Setting10x10.RewardFunctions.LinearFunctions import plane, noise
from Scenarios.Setting10x10.TenTimesTenEnvironment import TenTimesTenEnvironment
from Scenarios.Setting10x10.GameSimulator import simulate
from Scenarios.Setting10x10.dump_results import dump_results


runs, iterations_per_run = 200, 200
env = TenTimesTenEnvironment(reward_function=noise(plane(inclination=5, final_reward=100)))
# agent = ModularAgent(
#     estimator=MonteCarlo(),
#     value_update_rate="per_game",
#     policy=EpsilonGreedy(exploration_rate=step_function(200*120))
# )

agent2 = ModularAgent(
    estimator=TDLambda(),
    value_update_rate="per_step",
    policy=UCB(),
)
results, information = simulate(
    agent=agent2, environment=env, runs=runs, iterations_per_run=iterations_per_run)

directory = "./results"
columns = ["REWARD", "STATE", "ACTION", "ESTIMATE"]
directory_generated = dump_results(results, information, directory, columns)

print(directory_generated)
