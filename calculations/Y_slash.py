import numpy as np
from typing import Callable
from sympy import symbols, lambdify
from scipy.misc import derivative


def partial_derivative(func: Callable, var: int = 0, der_order: int = 1, point: tuple = ()):
    args = list(point[:])

    def wraps(x):
        args[var] = x
        return func(*args)

    return derivative(func=wraps, x0=point[var], dx=1e-6, n=der_order)


def Y_slash(y_infinity: Callable, Lr0_list: np.array, xl0_list: np.array, LrG_list: np.array,
            slG_list: np.array) -> np.array:
    """

    :param y_infinity: function of two variables
    :param Lr0_list: list of Lr0 differential operators that look like: L(f) -> sympy.diff(f, x) + ...
    :param xl0_list: list of float xl0: [x0, x1, x2, ...]
    :param LrG_list: list of LrG differential operators that look like: L(f) -> sympy.diff(f, x) + ...
    :param slG_list: list of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :return: np.array matrix of floats with L0*R0 + LG*RG rows and 1 col
    """
    # x = symbols('x')
    # t = symbols('t')

    L_0 = len(xl0_list)
    R_0 = len(Lr0_list)

    L_G = len(slG_list)
    R_G = len(LrG_list)

    Yrl = []
    for i in range(R_0):
        for j in range(L_0):

            Yrl.append(partial_derivative(y_infinity, 1, 1, (xl0_list[j], 0)))
            # Yrl.append(lambdify((x, t), Lr0_list[i](y_infinity(x, t)).subs([(x, xl0_list[j]), (t, 0)])))

    Ypl = []
    for i in range(R_G):
        for j in range(L_G):
            # Ypl.append(lambdify((x, t), LrG_list[i](y_infinity(x, t)).subs([(x, slG_list[j][0]), (t, slG_list[j][1])])))
            Ypl.append(partial_derivative(y_infinity, 0, 1, (slG_list[j][0], slG_list[j][1])))

    result = []
    for ii in range(R_0 * L_0):
        result.append([Yrl[ii]])
    for jj in range(R_G * L_G):
        result.append([Ypl[jj]])

    return np.array(result)
