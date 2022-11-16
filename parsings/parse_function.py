from typing import Callable
from sympy.parsing import parse_expr
from sympy import lambdify
from sympy.abc import x, t


def parse_function(function_string: str) -> Callable:
    sympy_function = parse_expr(function_string, transformations="all")

    print(f'Sympy function: {sympy_function}')

    return lambdify((x, t), sympy_function)