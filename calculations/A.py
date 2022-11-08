import numpy as np
from typing import Callable
from sympy import symbols, lambdify


def A(G: Callable, Lr0_list: np.array, xl0_list: np.array, LrG_list: np.array, slG_list: np.array) -> np.array:
    """

    :param G: function of two variables - Green's function
    :param Lr0_list: list of Lr0 differential operators that look like: L(f) -> sympy.diff(f, x) + ...
    :param xl0_list: list of float xl0: [x0, x1, x2, ...]
    :param LrG_list: list of LrG differential operators that look like: L(f) -> sympy.diff(f, x) + ...
    :param slG_list: list of slG that is np.array of two float values x and t: [[x0, t0], [x1, t1], ...]
    :return: np.array of A11, A12, A21, A22 that are np.arrays matrix of two variables functions
    """
    x = symbols('x')
    x_ = symbols('x_')
    t = symbols('t')
    t_ = symbols('t_')

    L_0 = len(xl0_list)
    R_0 = len(Lr0_list)

    L_G = len(xl0_list)
    R_G = len(Lr0_list)

    A11 = []
    for i in range(R_0):
        for j in range(L_0):
            A11.append([lambdify((x_, t_), Lr0_list[i](G(x - x_, t - t_)).subs([(x, xl0_list[j]), (t, 0)]))])
    A11 = np.array(A11)
    A12 = A11

    A21 = []
    for i in range(R_G):
        for j in range(L_G):
            A21.append(
                [lambdify((x_, t_), LrG_list[i](G(x - x_, t - t_)).subs([(x, slG_list[j][0]), (t, slG_list[j][1])]))])
    A21 = np.array(A21)
    A22 = A21

    return np.array([A11, A12, A21, A22])
