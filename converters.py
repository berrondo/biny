from copy import copy


class B(str):
    base = {'0b': 2, '0o': 8, '0x': 16}

    def __init__(self, byte, byte_width='{:b}'):
        super(B, self).__init__()
        prefix = '0b'
        if type(byte) is str:
            if byte.startswith(tuple(self.base.keys())):
                prefix = byte[:2]
                byte = byte_width.format(int(byte, self.base[prefix]))
            else:
                byte = byte_width.format(int(prefix+byte, self.base[prefix]))
        if type(byte) is int:
            byte = byte_width.format(byte)
        self.byte = tuple(map(int, byte))

    def __iter__(self):
        i = copy(self.byte)
        return iter(i)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return int(''.join(map(str, self.byte)), 2)

    def to_d(self):
        return self.__hash__()


class B4(B):
    def __init__(self, byte):
        super(B4, self).__init__(byte, '{:04b}')


class B8(B):
    def __init__(self, byte):
        super(B8, self).__init__(byte, '{:08b}')


assert B('10') == (1, 0)
assert B((1, 0)) == (1, 0)
assert B([1, 0]) == (1, 0)
assert B(('1', '0')) == (1, 0)
assert B(['1', '0']) == (1, 0)
assert B(0b10) == (1, 0)
assert B('0b10') == (1, 0)
assert B(2) == (1, 0)
assert B(0xF) == (1, 1, 1, 1)
assert B(0o10) == (1, 0, 0, 0)
assert B('0o10') == (1, 0, 0, 0)
assert B('0xF') == (1, 1, 1, 1)
# assert B('F') == (1, 1, 1, 1)

assert B8('0000') == (0, 0, 0, 0, 0, 0, 0, 0)
print(B8('0000').byte)
print(B('00000000').byte)
# assert B('00000000') == (0, 0, 0, 0, 0, 0, 0, 0)

def unpack(b0, b1, b2, b3, b4):
    return b0, b1, b2, b3, b4


assert unpack(*B(0x10)) == (1, 0, 0, 0, 0)


# def dec_to_bin(dec):
#     return map(int, bin(dec)[2:])


# def bin_to_dec(byte):
#     return int(''.join(map(str, byte)), 2)


# assert bin_to_dec(B('100')) == 4
# assert bin_to_dec(B((1, 0, 0)) == 4
