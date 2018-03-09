from rl.action import DiscreteAction
from rl.state import DiscreteState


class DiscreteAgentChoice:
    def __init__(self, state: DiscreteState, action_chosen: DiscreteAction):
        self.state = state
        self.action_chosen = action_chosen
