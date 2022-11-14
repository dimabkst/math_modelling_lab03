from view import View
from calculations import y_infinity, A, Y_slash, A_v, P, u_0, u_G, y_0, y_G, y, solve
import numpy as np
from typing import Callable
from scipy.misc import derivative


def partial_derivative(func: Callable, var: int = 0, der_order: int = 1, point: tuple = ()):
    args = list(point[:])

    def wraps(x):
        args[var] = x
        return func(*args)

    return derivative(func=wraps, x0=point[var], dx=1e-6, n=der_order)


def differential_operator(var: int = 0, der_order: int = 1):
    def derivative_of_func(func: Callable):
        def derivative_of_func_in_point(*point):
            args = list(point[:])

            def wraps(x):
                args[var] = x
                return func(*args)

            return derivative(func=wraps, x0=point[var], dx=1e-6, n=der_order)

        return derivative_of_func_in_point

    return derivative_of_func


if __name__ == "__main__":
    # View()
    def G(x_, t_):
        return x_ ** 2


    def u(x_, t_):
        return x_ * t_


    S0 = np.array([[0, 1]])
    T = 1

    Lr0_list = np.array([differential_operator(0, 1)])
    # print(operator(0, 1)(lambda x_, t_: x_ + x_*t_, (1, 1)))
    xl0_list = np.array([0.5, 1, 0.3])
    LrG_list = np.array([differential_operator(1, 1)])
    slG_list = np.array([[0.5, 1],
                         [0.25, 0.75]])

    v_0 = lambda x_, t_: x_ + t_
    v_G = lambda x_, t_: x_ - t_

    # res_A = A(G, Lr0_list, xl0_list, LrG_list, slG_list)
    # print(res_A[2][0][0](0.5, 0))
    # print(res_A)

    # res_y_infinity = y_infinity(G, u, S0, T)
    # print(res_y_infinity(1, 0))

    # res_Y_slash = Y_slash(res_y_infinity, Lr0_list, xl0_list, LrG_list, slG_list)

    # res_A_v = A_v(res_A, v_0, v_G, S0, T)
    #
    # res_P = P(res_A, S0, T)
    #
    # res_u_0 = u_0(res_A, res_P, res_Y_slash, res_A_v, v_0)
    # res_u_G = u_G(res_A, res_P, res_Y_slash, res_A_v, v_G)
    #
    # res_y_0 = y_0(G, S0, T, res_u_0)
    # res_y_G = y_G(G, S0, T, res_u_G)
    #
    # res_y = y(res_y_infinity, res_y_0, res_y_G)

    res_solve = solve(G, u, S0, T, Lr0_list, xl0_list, LrG_list, slG_list, v_0, v_G)

    print(res_solve)
