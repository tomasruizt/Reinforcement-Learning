import uuid
from typing import Iterable

from rl.action.action import Action
from rl.messages.Message import Message
from rl.state.state import State


class StateMessage(Message):
    """
    Message that the Environment send to the Agent communicating that it is in a new state.
    """

    def __init__(self, interaction_id: uuid.UUID, state: State, action_space: Iterable[Action]):
        """
        Initializes a Statemessage with the given input.
        :param interaction_id: The specific interaction, which will be referenced from now on with this UUID.
        :param state: The new state where the agent is in.
        :param action_space: The available actions for the Agent to choose from the state
        """
        self.state = state
        self.action_space = action_space
        super().__init__(interaction_id)
