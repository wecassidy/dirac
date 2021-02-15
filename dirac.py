from dataclasses import dataclass

from sympy.core.expr import Expr
from sympy.physics.quantum import Bra, Ket


@dataclass
class BraStart:
    lhs: Expr
    expr: Expr

    def __or__(self, rhs):
        if isinstance(rhs, KetEnd):
            rhs = Ket(rhs.expr) * rhs.rhs
        return self.lhs * Bra(self.expr) * rhs


@dataclass
class KetEnd:
    expr: Expr
    rhs: Expr

    def __ror__(self, lhs):
        if isinstance(lhs, BraStart):
            lhs = lhs.lhs * Bra(lhs.expr)
        return lhs * Ket(self.expr) * self.rhs


Expr.__lshift__ = lambda lhs, rhs: BraStart(lhs, rhs)
Expr.__rshift__ = lambda lhs, rhs: KetEnd(lhs, rhs)
