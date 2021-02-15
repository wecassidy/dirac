import sympy
from sympy import oo


class Bra(sympy.core.expr.Expr):
    def inner_product(self, ket, var):
        return sympy.integrate(sympy.conjugate(self) * ket, (var, -oo, oo))

    def __str__(self):
        return f"< {super().__str__()} |"


class Ket(sympy.core.expr.Expr):
    def __str__(self):
        return f"| {super().__str__()} >"
