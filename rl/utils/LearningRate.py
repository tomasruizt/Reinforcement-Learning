from itertools import count


def decaying(runs, iterations_per_run):
    """
    Decaying rate. Starts with 1 and after runs*iterations, the rate is 0.01.
    :param runs:
    :param iterations_per_run:
    :return: generator with decaying rate
    """
    # Solve x for:
    # 0.01 = 1 / (1 + runs * iterations / x)
    x = runs * iterations_per_run / (1 / 0.01 - 1)
    c = count()
    while True:
        yield 1/(1 + next(c)/x)


def linear_decay(runs, iterations_per_run):
    # Solve for x
    # y = ax + b
    # y(0) = 1
    # y(i*r) = 0.01
    c = count()
    while True:
        yield max(next(c) * (0.01-1)/(runs * iterations_per_run) + 1, 0.01)


def step_function(steps):
    step = 0
    while step <= steps:
        yield 1
        step += 1
    while True:
        yield 0
