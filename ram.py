from class_gates import NOT, AND
from flip_flop import Latch8
from opcodes import *


class RAM:
    def __init__(self):
        self._256x8_ = {B8(k): Latch8() for k in range(256)}  # 65536

    def addr(self, byte):
        return self._256x8_[byte]


Ram = RAM()
assert Ram.addr(B8('0000'))() == (0, 0, 0, 0, 0, 0, 0, 0)
assert Ram.addr(B8('0000')).in_(0, 0, 0, 0, 0, 0, 0, 1).w(1)() == (0, 0, 0, 0, 0, 0, 0, 1)

Ram.addr(B8('0000')).in_(*LOD).w(1)
Ram.addr(B8('0001')).in_(*STO).w(1)
Ram.addr(B8('0010')).in_(*SUB).w(1)
Ram.addr(B8('0011')).in_(*HLT).w(1)

assert Ram.addr(B8('0000')).out() == LOD
assert Ram.addr(B8('0001')).out() == STO
assert Ram.addr(B8('0010')).out() == SUB
assert Ram.addr(B8('0011')).out() == HLT


class Decoder_2x4:
    def __init__(self):
        self._addr1, self._addr2 = 0, 0
        self.NOT1 = NOT()
        self.NOT2 = NOT()
        self.AND1 = AND()
        self.AND2 = AND()
        self.AND3 = AND()
        self.AND4 = AND()

    def addr1(self, bit1):
        self._addr1 = bit1
        return self

    def addr2(self, bit2):
        self._addr2 = bit2
        return self

    def __out(self):
        self.NOT1.in_(self._addr1)
        self.NOT2.in_(self._addr2)
        self.o0 = self.AND1.in1(self.NOT1.out).in2(self.NOT2.out).out()
        self.o1 = self.AND2.in1(self._addr1).in2(self.NOT2.out).out()
        self.o2 = self.AND3.in1(self.NOT1.out).in2(self._addr2).out()
        self.o3 = self.AND4.in1(self._addr1).in2(self._addr2).out()

    def out(self):
        self.__out()
        return self.o0, self.o1, self.o2, self.o3


ram2 = Decoder_2x4()
assert ram2.addr1(0).addr2(0).out() == (1, 0, 0, 0)
assert ram2.addr1(0).addr2(1).out() == (0, 0, 1, 0)
assert ram2.addr1(1).addr2(0).out() == (0, 1, 0, 0)
assert ram2.addr1(1).addr2(1).out() == (0, 0, 0, 1)
