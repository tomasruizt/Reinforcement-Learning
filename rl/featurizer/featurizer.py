from rl.state import DiscreteState


class DiscreteFeaturizer:
    """
    The featurizer is responsible for mapping a reality described by the
    environment state into features that an ML model can understand.

    For example, a Scalar-Featurizer would take all the variables that
    describe a Poker hand and return a single scalar feature that can
    represent the score of that hand, which a simple ML model could use.

    A Vector-Featurizer would take the same variables that describe the
    Poker hand and output an n-dimensional array for a neural network.

    Different Featurizers can take different elements of the state into
    account. For example, a complex Scalar-Featurizer could look not only
    at the score of the hand, but also a cards on the table, at amount
    at stake or any other information available in the state and combine
    them in nonlinear ways to output the scalar feature.
    """

    def featurize(self, state: DiscreteState):
        """
        Maps the input state to features that the corresponding ML model
        can understand.
        :param state: The state whose features we want.
        :return: The features, which could be a scalar, an
        n-dimenstional array or other.
        """
        raise NotImplementedError
