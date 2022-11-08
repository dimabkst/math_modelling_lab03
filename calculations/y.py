import numpy as np
from typing import Callable
from calculations import y_infinity
from calculations import y_0
from calculations import y_G


def y(G: Callable, u: Callable, S0: np.array, T: float) -> Callable:
    """

    :param G: function of two variables - Green's function
    :param u: function of two variables - Disturbance
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space-time domain
    :param T: float greater that zero - Max time value
    :return: function of two variables
    """

    def res(x: float, t: float) -> float:
        return y_infinity(G, u, S0, T)(x, t) + y_0(G, S0, T)(x, t) + y_G(G, S0, T)(x, t)

    return res
