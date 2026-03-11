import numpy as np
import math


def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    e = math.e
    def _tanh(x):
        return (e ** x - (e ** (-x))) / ((e ** x) + (e ** (-x)))
    return _tanh(x)