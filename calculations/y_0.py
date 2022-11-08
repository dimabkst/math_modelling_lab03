import numpy as np
from typing import Callable
from scipy.integrate import dblquad
# from calculations import u_0


def y_0(G: Callable, S0: np.array, T: float) -> Callable:
    """

    :param G: function of two variables - Green's function
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]) - Space-time domain
    :param T: float greater that zero - Max time value
    :return: function of two variables
    """

    # u_0 = u_0(...)
    def u_0(x, t): return
    T_0 = -T

    def res(x: float, t: float) -> float:
        def integrand(x_: float,
                      t_: float) -> float:  # For using in scipy.integrate.dblquad and in formula G(x-x', t-t')u(x',t')
            return G(x - x_, t - t_) * u_0(x_, t_)

        integral = 0.0
        for i in range(len(S0)):
            integral += dblquad(integrand, T_0, 0, lambda t_: S0[i][0], lambda t_: S0[i][1])[0]  # Sec value is precision

        return integral

    return res
