from view import View
from calculations import y_infinity, A, Y_slash, A_v, P, u_0, u_G, y_0, y_G, y, solve
from parsings import parse_operator
import numpy as np
from typing import Callable
from scipy.misc import derivative


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
    # View testing
    # View()

    # ------------------------------------------------------------------------------------------------------------------

    # Calculations testing
    # def G(x_, t_):
    #     return x_ ** 2
    #
    #
    # def u(x_, t_):
    #     return x_ * t_
    #
    #
    # S0 = np.array([[0, 1]])
    # T = 1
    #
    # Lr0_list = np.array([differential_operator(0, 1)])
    # # print(operator(0, 1)(lambda x_, t_: x_ + x_*t_, (1, 1)))
    # xl0_list = np.array([0.5, 1, 0.3])
    # LrG_list = np.array([differential_operator(1, 1)])
    # slG_list = np.array([[0.5, 1],
    #                      [0.25, 0.75]])
    #
    # v_0 = lambda x_, t_: x_ + t_
    # v_G = lambda x_, t_: x_ - t_
    #
    # res_solve = solve(G, u, S0, T, Lr0_list, xl0_list, LrG_list, slG_list, v_0, v_G)
    #
    # print(res_solve)

    # ------------------------------------------------------------------------------------------------------------------

    # Parser testing
    operator_str = "4*d[x,1]-8*d[t,2]"
    res_parse_operator = parse_operator(operator_str)


    def parse_test_func(x: float, t: float):
        return x ** 2 + t ** 3


    print(res_parse_operator(parse_test_func)(1, 0))
