import math

from view import View
from calculations import y_infinity, A, Y_slash, A_v, P, u_0, u_G, y_0, y_G, y, solve
from parsings import parse_operator, parse_function, parse_S0
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
    print(f'Operator string: {operator_str}')
    res_parse_operator = parse_operator(operator_str)


    def parse_test_func(x: float, t: float):
        return x ** 2 + t ** 3


    x0, y0 = 1, 0
    print(f'Operator on function x^2 + t^3 value in ({x0}, {y0}):{res_parse_operator(parse_test_func)(1, 0)}')
    print()

    function_str1 = "sin(x)+t**2"
    print(f'Function string: {function_str1}')
    res_parse_function1 = parse_function(function_str1)
    x1, t1 = math.pi / 2, 1
    print(f'Function value in ({x1}, {t1}): {res_parse_function1(x1, t1)}')
    print()

    function_str2 = "(1/sqrt(4*pi*t))*exp(-x^2/(4*t))"
    # function_str2 = "(Piecewise((0, t<=0),(1, t>0))(t)/sqrt(4*pi*t))*exp(-x^2/(4*t))"
    # function_str2 = "(Heaviside(t)/sqrt(4*pi*t))*exp(-x^2/(4*t))"
    print(f'Function string: {function_str2}')
    res_parse_function2 = parse_function(function_str2)
    x2, t2 = math.pi / 2, 1
    print(f'Function value in ({x2}, {t2}): {res_parse_function2(x2, t2)}')
    print()

    S0_str = "[0, 1] v [2,3]  [4,5.5]"
    print(f'S0 string: {S0_str}')
    res_parse_S0 = parse_S0(S0_str)
    print(f'S0: {res_parse_S0}')
    print()
