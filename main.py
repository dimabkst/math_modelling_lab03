from view import View
from calculations import y_infinity, A, Y_slash, A_v, P
import numpy as np
from sympy import diff, symbols

if __name__ == "__main__":
    # View()
    def G(x_, t_):
        return x_ ** 2


    x = symbols('x')
    t = symbols('t')
    Lr0_list = np.array([lambda f: diff(f, t)])
    xl0_list = np.array([0.5, 1])
    LrG_list = np.array([lambda f: diff(f, x)])
    slG_list = np.array([[0.5, 1],
                         [0.25, 0.75]])

    res_A = A(G, Lr0_list, xl0_list, LrG_list, slG_list)
    print(res_A[2][0][0](0.5, 0))
    print(res_A)


    def u(x_, t_):
        return x_ * t_


    S0 = np.array([[0, 1]])
    T = 1
    y_inf = y_infinity(G, u, S0, T)
    print(y_inf(1, 0))

    print(Y_slash(y_inf, Lr0_list, xl0_list, LrG_list, slG_list))
    print(A_v(res_A, lambda x_, t_: x_ + t_, lambda x_, t_: x_ - t_, S0, T))

    print(P(res_A, S0, T))
