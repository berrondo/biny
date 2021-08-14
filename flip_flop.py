from function_gates import AND, NOT
from class_gates import NOR
from converters import B


class FlipFlop:
    def __init__(self):
        self._s, self._r = 0, 1
        self.q, self._q = 0, 1
        self.NOR1 = NOR()
        self.NOR2 = NOR()

    def s(self, bit):
        self._s = bit
        return self

    def r(self, bit):
        self._r = bit
        return self

    def out(self):
        self.NOR1.in1(self._s)
        self.NOR2.in1(self._r)
        self.NOR2.in2(self.NOR1.out)
        self.NOR1.in2(self.NOR2.out)
        self.q = self.NOR2.out()
        self._q = self.NOR1.out()

        return self.q, self._q

    def __call__(self):
        return self.out()


flipflop = FlipFlop()
#                 s    r        q _q
assert flipflop.s(1).r(0)() == (1, 0)
assert flipflop.s(0).r(0)() == (1, 0)
assert flipflop.s(0).r(1)() == (0, 1)
assert flipflop.s(0).r(0)() == (0, 1)
assert flipflop.s(1).r(1)() == (0, 0)


class Latch:
    def __init__(self):
        self.ff = FlipFlop()
        self._in, self._w = 0, 0

    def in_(self, in_):
        self._in = in_
        return self

    def w(self, w):
        self._w = w
        return self

    def out(self):
        self.ff.s(AND(self._w, self._in))
        self.ff.r(AND(self._w, NOT(self._in)))

        return self.ff()

    def __call__(self):
        return self.out()


latch = Latch()
#                 s    r            q _q
assert latch.in_(1).w(0)() == (0, 1)
assert latch.in_(0).w(0)() == (0, 1)
assert latch.in_(0).w(1)() == (0, 1)
assert latch.in_(0).w(0)() == (0, 1)
assert latch.in_(1).w(1)() == (1, 0)
assert latch.in_(0).w(1)() == (0, 1)


class Latch8:
    def __init__(self):
        self.l0 = Latch()
        self.l1 = Latch()
        self.l2 = Latch()
        self.l3 = Latch()
        self.l4 = Latch()
        self.l5 = Latch()
        self.l6 = Latch()
        self.l7 = Latch()

    def in_(self, d0, d1, d2, d3, d4, d5, d6, d7):
        self.l0.in_(d0)
        self.l1.in_(d1)
        self.l2.in_(d2)
        self.l3.in_(d3)
        self.l4.in_(d4)
        self.l5.in_(d5)
        self.l6.in_(d6)
        self.l7.in_(d7)
        return self

    def in0(self, i):
        self.l0.in_(i)
        return self
    def in1(self, i):
        self.l1.in_(i)
        return self
    def in2(self, i):
        self.l2.in_(i)
        return self
    def in3(self, i):
        self.l3.in_(i)
        return self
    def in4(self, i):
        self.l4.in_(i)
        return self
    def in5(self, i):
        self.l5.in_(i)
        return self
    def in6(self, i):
        self.l6.in_(i)
        return self
    def in7(self, i):
        self.l7.in_(i)
        return self

    def w(self, w):
        self.l0.w(w)
        self.l1.w(w)
        self.l2.w(w)
        self.l3.w(w)
        self.l4.w(w)
        self.l5.w(w)
        self.l6.w(w)
        self.l7.w(w)
        return self

    def __out(self):
        self.o0 = self.l0()[0]
        self.o1 = self.l1()[0]
        self.o2 = self.l2()[0]
        self.o3 = self.l3()[0]
        self.o4 = self.l4()[0]
        self.o5 = self.l5()[0]
        self.o6 = self.l6()[0]
        self.o7 = self.l7()[0]

    def out(self):
        self.__out()
        return (self.o0,
                self.o1,
                self.o2,
                self.o3,
                self.o4,
                self.o5,
                self.o6,
                self.o7)

    def __call__(self):
        return self.out()


latch8 = Latch8()
assert latch8.in_(0, 0, 0, 0, 1, 1, 1, 1).w(0)() == (0, 0, 0, 0, 0, 0, 0, 0)
assert latch8.in_(0, 0, 0, 0, 1, 1, 1, 1).w(1)() == (0, 0, 0, 0, 1, 1, 1, 1)
assert latch8.in_(1, 1, 1, 1, 0, 0, 0, 0).w(0)() == (0, 0, 0, 0, 1, 1, 1, 1)
assert latch8()                                  == (0, 0, 0, 0, 1, 1, 1, 1)
assert latch8.w(0)()                             == (0, 0, 0, 0, 1, 1, 1, 1)
# assert latch8.w(1)()                             == (1, 1, 1, 1, 0, 0, 0, 0)  # ??????
assert latch8.in_(1, 1, 1, 1, 0, 0, 0, 0).w(0)() == (0, 0, 0, 0, 1, 1, 1, 1)
assert latch8.in_(1, 1, 1, 1, 0, 0, 0, 0).w(1)() == (1, 1, 1, 1, 0, 0, 0, 0)
assert latch8.in_(*B('10001000')).w(1)()         == B('10001000')  #(1, 0, 0, 0, 1, 0, 0, 0)
