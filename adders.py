from function_gates import AND, OR, XOR
from converters import B


def HALF_ADDER(bit1, bit2):
    return AND(bit1, bit2), XOR(bit1, bit2)


def FULL_ADDER(bit1, bit2, carry_in=0):
    carry_out, sum_ = HALF_ADDER(bit1, bit2)
    carry_out2, sum_out = HALF_ADDER(carry_in, sum_)
    return OR(carry_out, carry_out2), sum_out


def FULL_ADDER_(bit1, bit2, carry_in=0):
    return AND(bit1, bit2), XOR(XOR(bit1, bit2), carry_in)


def ADDER2(byte1, byte2):
    a1, a2 = byte1
    b1, b2 = byte2
    carry_out, sum_ = FULL_ADDER(a2, b2)
    return (*FULL_ADDER(a1, b1, carry_out), sum_)


def ADDER4(byte1, byte2):
    a1, a2, a3, a4 = byte1
    b1, b2, b3, b4 = byte2
    carry_out4, sum4 = FULL_ADDER(a4, b4)
    carry_out3, sum3 = FULL_ADDER(a3, b3, carry_out4)
    carry_out2, sum2 = FULL_ADDER(a2, b2, carry_out3)
    return (*FULL_ADDER(a1, b1, carry_out2), sum2, sum3, sum4)


assert FULL_ADDER(0, 0) == (0, 0)
assert FULL_ADDER(0, 1) == (0, 1)
assert FULL_ADDER(1, 0) == (0, 1)
assert FULL_ADDER(1, 1) == (1, 0)
assert FULL_ADDER(1, 1, 1) == (1, 1)


class Inverter:
    def __init__(self):
        self._i = 0

    def in_(self, byte):
        self._byte = byte
        return self

    def inv(self, i):
        self._i = i
        return self

    def out(self):
        i0, i1, i2, i3, i4, i5, i6, i7 = self._byte
        _i = self._i
        return (
            XOR(i0, _i),
            XOR(i1, _i),
            XOR(i2, _i),
            XOR(i3, _i),
            XOR(i4, _i),
            XOR(i5, _i),
            XOR(i6, _i),
            XOR(i7, _i),
        )

    def __call__(self):
        return self.out()


inverter = Inverter()
assert inverter.in_(B('10101010')).inv(1)()            == (0, 1, 0, 1, 0, 1, 0, 1)
assert inverter.in_(B('10101010')).inv(0)()            == (1, 0, 1, 0, 1, 0, 1, 0)
assert inverter.in_((0, 0, 0, 0, 0, 0, 0, 0)).inv(1)() == (1, 1, 1, 1, 1, 1, 1, 1)
