from function_gates import OR, AND
from flip_flop import Latch8
from ram import Decoder_2x4


class Memory:
    def __init__(self):
        self.addresser = Decoder_2x4()
        self.l0 = Latch8()
        self.l1 = Latch8()
        self.l2 = Latch8()
        self.l3 = Latch8()
        self._w = 0
        self.A, self.B, self.C, self.D = 0, 0, 0, 0
        self.o0, self.o1, self.o2, self.o3, self.o4, self.o5, self.o6, self.o7 = 0, 0, 0, 0, 0, 0, 0, 0

    def addr(self, bit1, bit2):
        self.A, self.B, self.C, self.D = self.addresser.addr1(bit1).addr2(bit2).out()
        return self

    def in_(self, byte):
        self.l0.in_(*byte)
        self.l1.in_(*byte)
        self.l2.in_(*byte)
        self.l3.in_(*byte)
        return self

    def w(self, _w):
        self._w = _w
        self.l0.w(AND(self.A, self._w))()
        self.l1.w(AND(self.B, self._w))()
        self.l2.w(AND(self.C, self._w))()
        self.l3.w(AND(self.D, self._w))()
        return self

    def out(self):
        A, B, C, D = self.A, self.B, self.C, self.D
        l0, l1, l2, l3 = self.l0, self.l1, self.l2, self.l3
        self.o0 = OR(AND(l0.o0, A), AND(l1.o0, B), AND(l2.o0, C), AND(l3.o0, D))
        self.o1 = OR(AND(l0.o1, A), AND(l1.o1, B), AND(l2.o1, C), AND(l3.o1, D))
        self.o2 = OR(AND(l0.o2, A), AND(l1.o2, B), AND(l2.o2, C), AND(l3.o2, D))
        self.o3 = OR(AND(l0.o3, A), AND(l1.o3, B), AND(l2.o3, C), AND(l3.o3, D))
        self.o4 = OR(AND(l0.o4, A), AND(l1.o4, B), AND(l2.o4, C), AND(l3.o4, D))
        self.o5 = OR(AND(l0.o5, A), AND(l1.o5, B), AND(l2.o5, C), AND(l3.o5, D))
        self.o6 = OR(AND(l0.o6, A), AND(l1.o6, B), AND(l2.o6, C), AND(l3.o6, D))
        self.o7 = OR(AND(l0.o7, A), AND(l1.o7, B), AND(l2.o7, C), AND(l3.o7, D))
        return self.o0, self.o1, self.o2, self.o3, self.o4, self.o5, self.o6, self.o7


mem = Memory()
mem.addr(1, 0).in_((1, 0, 0, 0, 1, 1, 1, 1)).w(1)
assert mem.addr(1, 0).out() == (1, 0, 0, 0, 1, 1, 1, 1)
assert mem.o0 == 1
assert mem.addr(0, 0).out() == (0, 0, 0, 0, 0, 0, 0, 0)
assert mem.o0 == 0




# def in_(self, byte):
# b0, b1, b2, b3, b4, b5, b6, b7 = byte
# A, B, C, D = self.A, self.B, self.C, self.D

# l0.in0(b0).in1(b1).in2(b2).in3(b3).in4(b4).in5(b5).in6(b6).in7(b7) #.w(AND(A, self._w))
# l1.in0(b0).in1(b1).in2(b2).in3(b3).in4(b4).in5(b5).in6(b6).in7(b7) #.w(AND(B, self._w))
# l2.in0(b0).in1(b1).in2(b2).in3(b3).in4(b4).in5(b5).in6(b6).in7(b7) #.w(AND(C, self._w))
# l3.in0(b0).in1(b1).in2(b2).in3(b3).in4(b4).in5(b5).in6(b6).in7(b7) #.w(AND(D, self._w))

# latch = (A and l0) or (B and l1) or (C and l2) or (D and l3)
# # latch = OR(AND(A, l0), AND(B, l1), AND(C, l2), AND(D, l3))  # TypeError: unsupported operand type(s) for |: 'int' and 'Latch8'
# latch.in_(*byte).w(1)

# l0(), l1(), l2(), l3()
# return self
