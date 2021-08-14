from functools import reduce
from function_gates import NOT as _NOT, NOR as _NOR, AND as _AND, OR as _OR

class __Gate:
    def __init__(self, *args):
        self.bit1, self.bit2 = 0, 0
        if args:
            self.bit1, self.bit2 = args[0], args[1]
        self._in = list(args)
        self._out = 1

    def in1(self, bit1):
        self.bit1 = bit1() if callable(bit1) else bit1
        return self

    def in2(self, bit2):
        self.bit2 = bit2() if callable(bit2) else bit2
        return self

    def in_(self, bit):
        self._in.append(bit)
        return self

    def __call__(self):
        return self.out()


class OR(__Gate):
    def out(self):
        if self._in:
            return reduce(_OR, self._in)
        return _OR(self.bit1, self.bit2)


Or = OR()
assert Or.in_(0).in_(0).out() == 0
assert Or.in_(0).in_(1).out() == 1
assert Or.in_(1).in_(0).out() == 1
assert Or.in_(1).in_(1).out() == 1


class NOR(__Gate):
    def out(self):
        return _NOR(self.bit1, self.bit2)


assert NOR(0, 0).out() == 1
assert NOR(0, 1).out() == 0
assert NOR(1, 0).out() == 0
assert NOR(1, 1).out() == 0

assert NOR().in1(0).in2(0).out() == 1
assert NOR().in1(0).in2(1).out() == 0
assert NOR().in1(1).in2(0).out() == 0
assert NOR().in1(1).in2(1).out() == 0

Nor = NOR()
assert Nor.in1(0).in2(0).out() == 1
assert Nor.in1(0).in2(1).out() == 0
assert Nor.in1(1).in2(0).out() == 0
assert Nor.in1(1).in2(1).out() == 0


class AND(__Gate):
    def out(self):
        return _AND(self.bit1, self.bit2)


assert AND(0, 0).out() == 0
assert AND(0, 1).out() == 0
assert AND(1, 0).out() == 0
assert AND(1, 1).out() == 1

assert AND().in1(0).in2(0).out() == 0
assert AND().in1(0).in2(1).out() == 0
assert AND().in1(1).in2(0).out() == 0
assert AND().in1(1).in2(1).out() == 1

And = AND()
assert And.in1(0).in2(0).out() == 0
assert And.in1(0).in2(1).out() == 0
assert And.in1(1).in2(0).out() == 0
assert And.in1(1).in2(1).out() == 1


class NOT:
    def __init__(self):
        self._in = 0

    def in_(self, bit1):
        self._in = bit1
        return self

    def out(self):
        return _NOT(self._in)


Not = NOT()
assert Not.in_(0).out() == 1
assert Not.in_(1).out() == 0