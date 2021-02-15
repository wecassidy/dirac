import sympy


class Bra:
    def __init__(self, expression):
        self.expression = sympy.conjugate(expression)

    def inner_product(self, ket):
        return sympy.integrate(bra * ket.expression)


class Ket:
    def __init__(self, expression):
        self.expression = expression


class Operator:
    def __init__(self, expression):
        self.expression = expression
