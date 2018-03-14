from rl.value_approximator.StateActionValues import StateActionValues
from rl.value_approximator.ValueApproximator import ValueApproximator


class ContextFreeValueApproximator(ValueApproximator):
    def approximate_value(self, state: str, actions: str) -> StateActionValues:
        pass

    def update_approximation(
            self, start_state: str, start_action: str, reward: float, end_state: str,  end_action: str):
        pass
