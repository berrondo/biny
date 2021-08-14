from functools import reduce
from operator import or_


def NOT(bit):
    r = not bit
    if r: return 1
    return 0


def AND(bit1, bit2):
    return bit1 and bit2


def OR(*args):
    # return any(args)
    return reduce(or_, args)


def NAND(bit1, bit2):
    return NOT(AND(bit1, bit2))


def XOR(bit1, bit2):
    return AND(NAND(bit1, bit2),
               OR(bit1, bit2))


def NOR(bit1, bit2):
    return NOT(OR(bit1, bit2))


def XNOR(bit1, bit2):
    return NOT(XOR(bit1, bit2))


assert NOT(0) == 1
assert NOT(1) == 0

assert AND(0, 0) == 0
assert AND(0, 1) == 0
assert AND(1, 0) == 0
assert AND(1, 1) == 1

assert OR(0, 0) == 0
assert OR(0, 1) == 1
assert OR(1, 0) == 1
assert OR(1, 1) == 1

assert XOR(0, 0) == 0
assert XOR(0, 1) == 1
assert XOR(1, 0) == 1
assert XOR(1, 1) == 0

assert NAND(0, 0) == 1
assert NAND(0, 1) == 1
assert NAND(1, 0) == 1
assert NAND(1, 1) == 0

assert NOR(0, 0) == 1
assert NOR(0, 1) == 0
assert NOR(1, 0) == 0
assert NOR(1, 1) == 0

assert XNOR(0, 0) == 1
assert XNOR(0, 1) == 0
assert XNOR(1, 0) == 0
assert XNOR(1, 1) == 1
