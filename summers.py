from adders import FULL_ADDER
from converters import B, B8


def binary_sum(byte1, byte2):
    summed = []
    carry_out = 0
    for bit1, bit2 in reversed(list(zip(byte1, byte2))):
        carry_out, sum_ = FULL_ADDER(bit1, bit2, carry_out)
        summed.append(sum_)
    summed.append(carry_out)
    return tuple(reversed(summed))


def decimal_sum(dec1, dec2):
    return B(binary_sum(B(dec1), B(dec2))).to_d()


assert binary_sum((0, 0),
                  (0, 0)) \
            == (0, 0, 0)

assert binary_sum((1, 0),
                  (1, 0)) \
            == (1, 0, 0)

assert binary_sum((1, 0),
                  (1, 1)) \
            == (1, 0, 1)

assert binary_sum((1, 1),
                  (1, 1)) \
            == (1, 1, 0)

assert binary_sum((1, 1, 0, 0),
                  (1, 1, 0, 1)) \
            == (1, 1, 0, 0, 1)

assert binary_sum((0, ), (0, )) == (0, 0)
assert binary_sum((0, 0), (0, 0)) == (0, 0, 0)
assert binary_sum((0, 0, 0), (0, 0, 0)) == (0, 0, 0, 0)
# assert binary_sum(B('00000000'), B('00000000')) == (0, 0, 0, 0, 0, 0, 0, 0, 0)

assert binary_sum(B8('00010000'), B8('11')) == (0, 0, 0, 1, 0, 0, 1, 1)

assert decimal_sum(0, 0) == 0
assert decimal_sum(15, 14) == 29
assert decimal_sum(31, 28) == 59
assert decimal_sum(3000004, 3000005) == 6000009
