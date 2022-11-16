from typing import Callable
import numpy as np
from calculations import y_infinity, A, Y_slash, A_v, P, u_0, u_G, y_0, y_G, y


def solve(G: Callable, u: Callable, S0: np.array, T: float,
          Lr0_list: np.array, xl0_list: np.array, LrG_list: np.array, slG_list: np.array,
          v_0: Callable, v_G: Callable) -> Callable:
    """

    :param G: function of two variables x, t - Green's function
    :param u: function of two variables x, t - Disturbance
    :param S0: has next form: np.array([[a0, b0],...,[a_last, b_last]]) - Space-time domain
    :param T: float greater that zero - Max time value
    :param Lr0_list: list of Lr0 differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param xl0_list: list of float xl0: [x0, x1, x2, ...]
    :param LrG_list: list of LrG differential operators that look like: L(f) -> scipy.derivative(f) + ...
    :param slG_list: list of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :param v_0: function of two variables x, t
    :param v_G: function of two variables x, t
    :return: function of 2 variables x, t
    """

    res_y_infinity = y_infinity(G, u, S0, T)
    res_A = A(G, Lr0_list, xl0_list, LrG_list, slG_list)
    res_Y_slash = Y_slash(res_y_infinity, Lr0_list, xl0_list, LrG_list, slG_list)
    res_A_v = A_v(res_A, v_0, v_G, S0, T)
    res_P = P(res_A, S0, T)
    res_u_0 = u_0(res_A, res_P, res_Y_slash, res_A_v, v_0)
    res_u_G = u_0(res_A, res_P, res_Y_slash, res_A_v, v_G)
    res_y_0 = y_0(G, S0, T, res_u_0)
    res_y_G = y_G(G, S0, T, res_u_G)
    res_y = y(res_y_infinity, res_y_0, res_y_G)

    return res_y
