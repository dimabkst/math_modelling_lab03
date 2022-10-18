from view import View
from calculations import y_infinity
import numpy as np

if __name__ == "__main__":
    # View()
    def G(x, t):
        return x + t


    def u(x, t):
        return x * t

    S0 = np.array([[0, 1]])
    T = 1
    print(y_infinity(G, u, S0, T)(5, 4))
