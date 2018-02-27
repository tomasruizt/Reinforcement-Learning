import random


def plane(final_reward=10, inclination=1):
    def f(x1, x2):
        if x1 == 9 and x2 == 9:
            return final_reward
        else:
            value = 1 / 2 + x1 / 18 - x2 / 18
            return value * inclination - 2*inclination
    return f


def noise(reward_function, sigma=1):
    def f(x1, x2):
        return random.normalvariate(mu=reward_function(x1, x2), sigma=sigma)
    return f

# Appendix:
# Calculating the reward function.
#
# r(x1, x2) = x1*w1 + x2+w2 +w3
# r(0,0) = r(9,9) <->
# w3 = w3 + 9w1 + 9w2 <->
# w2 = -w1
#
# r(9,0) = 1 <->
# 1 = 9w1 +w3
#
# r(0,9) = 0 <->
# 0 = -9w1 + w3
#
# -> 1 = 2w3 <->
# w3 = 1/2
#
# -> w1 = 1/18
# -> w2 = -1/18