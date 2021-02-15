from dataclasses import dataclass

from sympy.core.expr import Expr
from sympy.physics.quantum import Bra, Ket


@dataclass
class Pipe:
    lhs: Expr
    rhs: Expr


def start_bra(old_lt, lhs, rhs):
    if isinstance(rhs, Pipe):
        return lhs * Bra(rhs.lhs)
    else:
        return old_lt(lhs, rhs)


def end_ket(old_gt, lhs, rhs):
    if isinstance(lhs, Pipe):
        return Ket(lhs.rhs) * rhs
    else:
        return old_gt(lhs, rhs)


old_expr_le = Expr.__le__
old_expr_gt = Expr.__gt__

Expr.__le__ = lambda lhs, rhs: start_bra(old_expr_le, lhs, rhs)
Expr.__gt__ = lambda lhs, rhs: end_ket(old_op_gt, lhs, rhs)
Expr.__or__ = lambda lhs, rhs: Pipe(lhs, rhs)
