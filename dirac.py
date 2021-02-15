from dataclasses import dataclass

import sympy
from sympy.core.expr import Expr
from sympy.physics.quantum import Bra, Ket


@dataclass
class Pipe:
    lhs: Expr
    rhs: Expr


def start_bra(old_lt, lhs, rhs):
    print(lhs, rhs)
    if isinstance(rhs, Pipe):
        return lhs * Bra(rhs.lhs)
    else:
        return old_lt(lhs, rhs)


def end_ket(old_gt, lhs, rhs):
    if isinstance(lhs, Pipe):
        return Ket(lhs.rhs) * rhs
    else:
        return old_gt(lhs, rhs)


def pipe(old_or, lhs, rhs):
    return Pipe(lhs, rhs)
