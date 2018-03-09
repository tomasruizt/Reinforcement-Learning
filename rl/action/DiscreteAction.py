class DiscreteAction:
    """
    A simple representation of a discrete action with a name.
    """

    def __init__(self, name: str):
        """
        Initializes an action with a specific name.
        :param name: Name of the action.
        """
        input_type = type(name)
        assert input_type is str, "Input 'name' should be a string but is '%s'" % input_type
        self.name = name
