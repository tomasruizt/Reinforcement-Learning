import uuid


class Message:
    """
    The message is a container class with which the agent will communicate with its environment.
    """

    def __init__(self, interaction_id: uuid.UUID):
        """
        Initialize a Message with a reference UUID to a specific interaction between the agent and the environment.
        :param interaction_id: The reference to the specific interaction.
        """
        self.interaction_id = interaction_id
