import uuid

from rl.action.action import Action
from rl.messages.Message import Message


class ActionMessage(Message):
    """
    Message emitted by the agent as a response to a new state.
    """

    def __init__(self, interaction_id: uuid.UUID, action: Action):
        """
        Initilaizes an ActionMessage additionally with the action that the agent wants to communicate.
        :param interaction_id: The reference to the specific interaction.
        :param action: The action that the agent chose.
        """
        self.action = action
        super().__init__(interaction_id)

