import numpy as np


def z_meshgrid_gen(X, Y, values):
    """
    This function generates Z for 3d plotting based on a values
    dictionary, which contains the values in "string tuples".
    :param X:
    :param Y:
    :param values:
    :return:
    """
    assert X.shape == Y.shape
    assert len(X.shape) == 2

    z = np.zeros(X.shape)
    for row1, row2 in zip(X, Y):
        for i in row1:
            for j in row2:
                z[i, j] = values.get((i, j).__str__(), 0)
    return z
