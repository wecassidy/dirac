import sympy
from sympy import oo


class Bra:
    def __init__(self, expression):
        self.expression = sympy.conjugate(expression)

    def inner_product(self, ket, var):
        return sympy.integrate(self.expression * ket.expression, (var, -oo, oo))


class Ket:
    def __init__(self, expression):
        self.expression = expression


class Operator:
    def __init__(self, expression):
        self.expression = expression
